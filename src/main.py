import logging
import os
import uuid
from jinja2 import Environment, FileSystemLoader
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    send_from_directory,
    session,
    redirect,
)
from utils import (
    create_latex_document,
    generate_pdf,
    MealBuilder,
)
from db import create_db, get_all_recipes, seed_recipes


# Create the DB if it doesn't exist
create_db()
recipes = get_all_recipes()
if len(recipes) == 0:
    seed_recipes()


app = Flask(__name__)

# Load environment variables from the .env file
if os.getenv("GF_ENV", "development") == "development":
    from dotenv import load_dotenv

    load_dotenv()

app.logger = logging.getLogger("groceryflow")
app.logger.setLevel(logging.INFO)

if not app.logger.handlers:
    handler = logging.StreamHandler()  # Log to stderr
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("[%(asctime)s] [%(levelname)s]: %(message)s")
    handler.setFormatter(formatter)
    app.logger.addHandler(handler)

app.config["GF_ENV"] = os.getenv("GF_ENV", "development")
app.config["GF_OUTPUT_DIR"] = os.getenv("GF_FILE_GEN_OUTPUT_DIR")
os.makedirs(app.config["GF_OUTPUT_DIR"], exist_ok=True)

app.secret_key = os.getenv("GF_SESSION_KEY")
app.config["GF_RECIPE_DIR"] = os.getenv("GF_RECIPE_DIR")
app.config["GF_PRINTABLE_TEX_TEMPLATE_PATH"] = os.path.join(
    ".", "files", "template.tex"
)


@app.route("/document_readiness/<doc_id>", methods=["GET"])
def document_readiness(doc_id):
    try:
        uuid_obj = uuid.UUID(doc_id)
        if os.path.isfile(f"{app.config['GF_OUTPUT_DIR']}/{str(uuid_obj)}.pdf"):
            return jsonify({"status": "available"})
        else:
            return jsonify({"status": "not found"})

    except (ValueError, TypeError):
        return jsonify({"status": "invalid payload"})


@app.route("/documents/<doc_id>", methods=["GET"])
def fetch_document(doc_id):
    return send_from_directory(app.config["GF_OUTPUT_DIR"], doc_id)


@app.route("/", methods=["GET"])
def index():
    username = session.get("username")
    if username is None:
        return redirect("/login")

    recipes = get_all_recipes()
    # js_context = {"pending_document": "38aeafca-80e1-4496-b584-354fb5bb07c4"}
    js_context = {}
    return render_template("index.html", recipes=recipes, js_context=js_context)


@app.route("/", methods=["POST"])
def submit():
    username = session.get("username")
    if not username:
        return redirect("/login")

    selected_items = request.form.getlist("items")
    all_recipes = get_all_recipes()
    recipes = [recipe for recipe in all_recipes if str(recipe["id"]) in selected_items]

    filename = str(uuid.uuid4())
    (meals, all_ingredients) = MealBuilder().select_meals(recipes)

    tex_path = os.path.join("/tmp", "files", f"{filename}.tex")
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(app.config["GF_PRINTABLE_TEX_TEMPLATE_PATH"])

    create_latex_document(template, tex_path, meals, all_ingredients, app.logger)
    pdf_filepath = generate_pdf(tex_path, app.logger)

    js_context = {"pending_document": filename}
    return render_template("index.html", recipes=all_recipes, js_context=js_context)


@app.route("/login", methods=["GET"])
def login():
    return render_template("login.html")


@app.route("/login", methods=["POST"])
def attempt_login():
    username = request.form.get("username")
    password = request.form.get("password")

    if username == "robers" and password == "halley":
        session["username"] = "robers"
        return redirect("/")

    return render_template("login.html")


if __name__ == "__main__":
    app.run()
