import logging
import os
import uuid
from dotenv import load_dotenv
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
    get_recipes,
    create_latex_document,
    generate_pdf,
    MealBuilder,
)

# Load environment variables from the .env file
load_dotenv()

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[logging.StreamHandler(), logging.FileHandler("app.log")],
)


@app.route("/document_readiness/<doc_id>", methods=["GET"])
def document_readiness(doc_id):
    try:
        uuid_obj = uuid.UUID(doc_id)
        if os.path.isfile(f"{app.config['output_dir']}/{str(uuid_obj)}.pdf"):
            return jsonify({"status": "available"})
        else:
            return jsonify({"status": "not found"})

    except (ValueError, TypeError):
        return jsonify({"status": "invalid payload"})


@app.route("/documents/<doc_id>", methods=["GET"])
def fetch_document(doc_id):
    return send_from_directory(app.config["output_dir"], doc_id)


@app.route("/", methods=["GET"])
def index():
    username = session.get("username")
    if username is None:
        return redirect("/login")

    # js_context = {"pending_document": "38aeafca-80e1-4496-b584-354fb5bb07c4"}
    js_context = {}
    return render_template("index.html", recipes=app.recipes, js_context=js_context)


@app.route("/", methods=["POST"])
def submit():
    username = session.get("username")
    if not username:
        return redirect("/login")

    filename = str(uuid.uuid4())
    selected_items = request.form.getlist("items")

    meal_fps = [
        os.path.join(app.config["RECIPE_DIR"], recipe) for recipe in selected_items
    ]
    (meal_idx, items) = MealBuilder().select_meals(meal_fps)

    tex_path = os.path.join("/tmp", "files", f"{filename}.tex")
    env = Environment(loader=FileSystemLoader("."))
    template = env.get_template(app.config["printable_tex_template_path"])

    create_latex_document(template, tex_path, meal_idx, items, logger=app.logger)
    pdf_filepath = generate_pdf(tex_path, logger=app.logger)

    js_context = {"pending_document": filename}
    return render_template("index.html", recipes=app.recipes, js_context=js_context)


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


app.config["output_dir"] = os.getenv("FILE_GEN_OUTPUT_DIR")
os.makedirs(app.config["output_dir"], exist_ok=True)

app.secret_key = os.getenv("SESSION_KEY")
app.config["RECIPE_DIR"] = os.getenv("RECIPE_DIR")
app.config["printable_tex_template_path"] = os.path.join(".", "files", "template.tex")
app.recipes = get_recipes(app.config["RECIPE_DIR"])

if __name__ == "__main__":
    app.run()
