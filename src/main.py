import logging
import os
import uuid
from jinja2 import Environment, FileSystemLoader
from flask import Flask, render_template, request, jsonify, send_from_directory
from utils import get_printer_name, get_recipes, create_latex_document, generate_pdf, MealBuilder

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
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
    print(app.config["output_dir"])
    print(doc_id)
    return send_from_directory(app.config["output_dir"], doc_id)


@app.route("/", methods=["GET"])
def index():
    get_printer_name(logger=app.logger)

    # js_context = {"pending_document": "38aeafca-80e1-4496-b584-354fb5bb07c4"}
    js_context = {}
    return render_template('index.html', recipes=app.recipes, js_context=js_context)


@app.route("/", methods=["POST"])
def submit():
    filename = str(uuid.uuid4())
    selected_items = request.form.getlist("items")

    meal_fps = [os.path.join(app.config["recipe_dir"], recipe) for recipe in selected_items]
    (meal_idx, items) = MealBuilder().select_meals(meal_fps)

    tex_path = os.path.join("/tmp", "files", f"{filename}.tex")
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template(app.config["printable_tex_template_path"])

    create_latex_document(template, tex_path, meal_idx, items, logger=app.logger)
    pdf_filepath = generate_pdf(tex_path, logger=app.logger)

    js_context = {"pending_document": filename}
    return render_template('index.html', recipes=app.recipes, js_context=js_context)


app.config["output_dir"] = os.path.join("/tmp", "files")
os.makedirs(app.config["output_dir"], exist_ok=True)

app.config["recipe_dir"] = "/home/jake/Code/project-recipe/recipes"
app.config["printable_tex_template_path"] = os.path.join(".", "files", "template.tex")
app.recipes = get_recipes(app.config['recipe_dir'])

if __name__ == "__main__":
    app.run()
