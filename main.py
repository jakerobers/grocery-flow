"""
User feedback
    I'd like to more easily be able to add recipes
    I'd like to more easily validate recipes that were added
    I'd like to provide my own master list of item ordering so that the list order matches the order that I get stuff at the store
    I'd like to use this on my phone
    Instead of printing, I'd like to send the order to Doordash or Aldi for pickup

For sharing with others:
    How do we package this up as a one-click install app. Would like desktop icon for easy execution.
    Move the ./recipes outside of this repo so that you can publish it to github and let others add their own recipes
    Eventually we can make a static site generator to make these publicly accessible

For collaborating
    figure out configuring sphinx to use the comments in this code

Things that will naturally arise as needs
    split this out into an app directory
    add unit tests
"""

import json
import subprocess
import re
import os
import argparse
import logging

import tkinter as tk
from tkinter import messagebox
from jinja2 import Environment, FileSystemLoader

CLEAN_INGREDIENT_PTN = r"^(to taste|to serve|[\d]+(?:\.\d+)?(?:\s(?:diced|oz|cups?|cloves?|grams?|teaspoons?|pinches?|packages?|tablespoons?|sliced|grated|ground|melted|ounces|lb|minced|tbsp|tsp|bunch|chopped|halved|scoop|juiced|pounds|stalks?|pinch|cans?|squeezed))*)\s*"

# TODO: make this configurable from the UI
PINNED_RECIPES = [
    "bean_stuff.md",
    "mexican_quinoa.md"
]



class RecipeSelectorGUI:
    def __init__(self, master, recipe_dir="./recipes", printer_name=None, output_filename=None, conf=None, logger=None):
        self.master = master
        self.logger=logger
        self.recipe_dir = recipe_dir
        self.printer_name=printer_name
        self.output_filename = output_filename
        self.conf = conf
        self.selected_recipes = []

        # Set up the window
        master.title("Recipe Selector")
        master.geometry("600x600")

        # Title Label
        title_label = tk.Label(master, text="Select Your Meals", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Scrollable Frame for Checkboxes
        self.checkbox_frame = tk.Frame(master)
        self.checkbox_frame.pack(fill="both", expand=True, padx=10)

        self.canvas = tk.Canvas(self.checkbox_frame)
        self.canvas.bind_all("<MouseWheel>", self._on_mouse_wheel)  # For Windows and macOS
        # For Linux, you may need to use <Button-4> and <Button-5> events
        self.canvas.bind_all("<Button-4>", self._on_mouse_wheel)
        self.canvas.bind_all("<Button-5>", self._on_mouse_wheel)

        self.scrollbar = tk.Scrollbar(self.checkbox_frame, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = tk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

        # Add checkboxes for each recipe
        self.recipe_vars = []
        for recipe in self.get_recipes():
            var = tk.BooleanVar()
            checkbox = tk.Checkbutton(self.scrollable_frame, text=recipe[1], variable=var)
            checkbox.pack(anchor="w", padx=10, pady=2)
            self.recipe_vars.append((var, recipe))

        # Submit Button
        submit_button = tk.Button(master, text="Submit", command=self.submit_selection)
        submit_button.pack(pady=10)


    def _on_mouse_wheel(self, event):
        if event.num == 5 or event.delta == -120:
            self.canvas.yview_scroll(1, "units")  # Scroll down
        elif event.num == 4 or event.delta == 120:
            self.canvas.yview_scroll(-1, "units")  # Scroll up

    def get_recipes(self):
        """Retrieve a list of RecipeMD files from the recipes directory."""
        meal_files = [f for f in os.listdir(self.recipe_dir) if f.endswith(".md")]
        pinned_meal_files = [x for x in meal_files if x in PINNED_RECIPES]
        unpinned_meal_files = [x for x in meal_files if x not in PINNED_RECIPES]
        meal_files = pinned_meal_files + unpinned_meal_files

        meal_names = []
        for meal_file in meal_files:
            meal_fp = os.path.join(".", "recipes", meal_file)
            meal_name = subprocess.run(
                ["recipemd", meal_fp, "-t"],
                capture_output=True,
                text=True
            ).stdout

            meal_name = meal_name.strip()
            if meal_file in pinned_meal_files:
                meal_name = f"^ {meal_name}"

            meal_names.append((meal_file, meal_name))

        return meal_names


    def submit_selection(self):
        """Collect and show the selected recipes."""
        self.selected_recipes = [recipe[0] for var, recipe in self.recipe_vars if var.get()]
        ProcessSelection(self.conf, self.printer_name).execute(self.selected_recipes, self.output_filename)

        # Show the selected recipes in a messagebox
        if self.selected_recipes:
            messagebox.showinfo("Selected Recipes", "Selected recipes:\n" + "\n".join(self.selected_recipes))
        else:
            messagebox.showinfo("No Selection", "No recipes selected.")


class ProcessSelection:
    def __init__(self, conf, printer_name):
        self.conf = conf
        self.printer_name = printer_name

    def execute(self, selected_recipes, output_filename):
        meal_fps = [os.path.join(".", "recipes", recipe) for recipe in selected_recipes]
        (meal_idx, items) = self._select_meals(meal_fps)
        logger.info(f"Using meals: {json.dumps(meal_idx)}")
        logger.info(f"Produced ingredient deck: {json.dumps(items)}")

        self._create_latex_document(meal_idx, items, logger=logger)
        self._generate_latex_file(logger=logger)
        self._print_pdf(output_filename, self.printer_name, dry_run=self.conf.dry_run, logger=logger)
        logger.info("Sent to printer...")


    def _select_meals(self, meal_fps, logger=None):
        """
        meal_fps: A collection of `os.path.join(".", "recipes", ".......")`
        """

        meal_idx = {}
        letter = 65 # A
        for meal_fp in meal_fps:
            meal_name = subprocess.run(
                ["recipemd", meal_fp, "-t"],
                capture_output=True,
                text=True
            ).stdout


            meal_title = meal_name.replace("\n", "")
            meal_idx[meal_fp] = {
                'title': meal_title,
                'short_code': chr(letter),
                'ingredients': []
            }
            letter += 1


        ingredients = []

        for meal_fp in meal_fps:
            meal_ingredients = subprocess.run(
                ["recipemd", meal_fp, "-i"],
                capture_output=True,
                text=True
            ).stdout

            meal_ingredient_items = meal_ingredients.split("\n")

            for mi in meal_ingredient_items:
                if re.search(r"^to taste", mi) is not None:
                    # Don't print out common ingredients like salt pepper, etc.
                    # Can make this configurable in the future if we want.
                    continue

                if self._in_reject_list(mi):
                    continue

                cleaned_ingredient = re.sub(CLEAN_INGREDIENT_PTN, "", mi).strip()
                meal_idx[meal_fp]['ingredients'].append(cleaned_ingredient)
                ingredients.append(cleaned_ingredient)

        sorted_unique_ingredients = list(sorted(set(ingredients)))

        # Go through and tag each ingredient to its corresponding meals.
        # This way when you're looking at the shopping list, you can easily
        # tell from a glance which ingredient corresponds to which meal(s)
        tagged_ingredients = []
        for i in sorted_unique_ingredients:
            meal_tag = []

            for _k, v in meal_idx.items():
                if i in v['ingredients']:
                    meal_tag.append(v['short_code'])

            tagged_ingredients.append(f"{i} ({','.join(meal_tag)})")

        return (meal_idx, tagged_ingredients)

    def _in_reject_list(self, ingredient):
        REJECT_LIST = [r".*water.*"] # Things to omit from a shopping list
        if ingredient.strip() == "":
            return True

        for r in REJECT_LIST:
            if re.search(r, ingredient) is not None:
                return True

        return False


    def _create_latex_document(self, meal_idx, items, logger=None):
        logger.info("Creating generated-list.tex using template.tex")
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(os.path.join(".", "files", "template.tex"))

        meals = []
        for _k, v in meal_idx.items():
            meals.append(f"({v['short_code']}) {v['title']}")

        data = { 'items': items, 'meals': meals }
        filled_template = template.render(data)

        with open(os.path.join(".", "files", "generated-list.tex"), "w") as f:
            f.write(filled_template)

    def _generate_latex_file(self, logger=None):
        logger.info("Generating latex file")
        file_path = os.path.join(".", "files", "generated-list.tex")
        file_dir = os.path.join(".", "files")
        subprocess.run(["pdflatex", f"-output-directory={file_dir}", file_path], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def _print_pdf(self, file_path, printer_name, dry_run=False, logger=None):
        if dry_run:
            logger.info("Dry-running the print job")
            return

        try:
            # Adjust paper size and other settings as needed
            subprocess.run([
                "lp",
                "-d", printer_name,          # Specify the printer by its name
                "-o", "media=Custom.4x5in",  # Set custom paper size
                "-o", "fit-to-page",         # Fit content to the page (optional)
                "-o", "print-quality=5",         # High print quality (5 is generally highest)
                "-o", "ColorModel=Gray",         # Monochrome (grayscale)
                "-o", "print-color-mode=monochrome",  # Force monochrome mode (redundant, but ensures grayscale)
                "-o", "cpi=12",                  # Characters per inch (CPI), optimized for text readability
                "-o", "resolution=150dpi",        # Lower DPI for faster print (try 72dpi if available)
                file_path                    # Path to the PDF file
            ], check=True)
            logger.info("Print job sent successfully.")
        except subprocess.CalledProcessError as e:
            logger.exception("Error sending print job")


def setup_logger():
    # Create a custom logger
    logger = logging.getLogger("PrintLogger")
    logger.setLevel(logging.INFO)

    # Create handlers
    file_path = os.path.join(".", "files", "print_job.log")
    file_handler = logging.FileHandler(file_path)
    console_handler = logging.StreamHandler()

    # Set logging level for each handler
    file_handler.setLevel(logging.INFO)
    console_handler.setLevel(logging.INFO)

    # Define log message format
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger


def get_printer_name(logger=None):
        # printer {{name}} is idle.  enabled since {{datetime}}
        lpstat_output = subprocess.run(
            ["lpstat", "-p"],
            capture_output=True,
            text=True
        ).stdout

        pattern = r"printer (\S+)"
        match = re.search(pattern, lpstat_output)

        if match:
            printer_name = match.group(1)
            logger.info(f"Will send print to {printer_name}")
            return printer_name
        else:
            logger.error("No printer found.")
            return None


def precleaning(pdf_filepath, logger=None):
    logger.info(f"Removing {pdf_filepath}")
    try:
        os.remove(pdf_filepath)
    except FileNotFoundError:
        pass


if __name__ == "__main__":
    """
     Getting Started
    ---------------

    .. code-block:: bash

        sudo apt install python3-tk
        sudo apt install tk-dev
        asdf uninstall python 3.13.0
        asdf install python 3.13.0


    .. code-block:: bash

        pip3 install textual
        pip3 install jinja2
        pip3 install recipemd
        pip3 install sphinx
        pip3 install openai


     Maintenance
    ---------------

    Generate the docs with the following.

    .. code-block:: bash

        make html


    Helpful Notes
    -------------

    - Edit ``./files/template.tex`` if you need to adjust the template
    """
    parser = argparse.ArgumentParser(description="Print a PDF file to a LAN printer.")
    parser.add_argument("--dry-run", action="store_true", help="Simulate the print job without sending it to the printer")
    args = parser.parse_args()

    logger = setup_logger()

    logger.info("Starting program...")

    printer_name = get_printer_name(logger=logger)
    if printer_name is None:
        logger.info("Exiting early since printer not found")

    pdf_filepath = os.path.join(".", "files", "generated-list.pdf")
    precleaning(pdf_filepath, logger=logger) # Cleans up dirty files as a sanity check

    root = tk.Tk()
    app = RecipeSelectorGUI(root, printer_name=printer_name, output_filename=pdf_filepath, conf=args, logger=logger)
    root.mainloop()
