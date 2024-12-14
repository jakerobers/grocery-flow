import logging
from flask import Flask, render_template, request
from utils import get_printer_name, get_recipes

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler("app.log")
    ]
)

@app.route("/", methods=["GET"])
def index():
    get_printer_name(logger=app.logger)
    return render_template('index.html', recipes=app.recipes)

@app.route("/", methods=["POST"])
def submit():
    print(request.form.getlist("items"))
    return render_template('index.html', recipes=app.recipes)

if __name__ == "__main__":
    app.config["recipe_dir"] = "/home/jake/Code/project-recipe/recipes"
    app.recipes = get_recipes(app.config['recipe_dir'])
    app.run()
