#!/usr/bin/env python3

"""
For really being able to use it
    OCR recipe cards to store in a document-driven data store
    OCR / GPT pipeline that can take a list of photos and convert it to recipemd files

For sharing with others:
    Add an installer that adds a desktop icon for easy execution
    Move the ./recipes outside of this repo so that you can publish it to github and let others add their own recipes

For collaborating
    figure out configuring sphinx to use the comments in this code
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

# CLEAN_INGREDIENT_PTN = r"^(to taste|[\d]+(?:\.\d+)?(diced| oz| cups?| cloves?| grams?| teaspoons?| pinches?| packages?| tablespoons?|sliced|ground|melted|ounces)?(| grated)?)\s*"

CLEAN_INGREDIENT_PTN = r"^(to taste|[\d]+(?:\.\d+)?(?:\s(?:diced|oz|cups?|cloves?|grams?|teaspoons?|pinches?|packages?|tablespoons?|sliced|grated|ground|melted|ounces|lb|minced|tbsp|tsp|bunch|chopped|halved|scoop|juiced|pounds|stalk|pinch))*)\s*"



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
        title_label = tk.Label(master, text="Select Recipes", font=("Helvetica", 16))
        title_label.pack(pady=10)

        # Scrollable Frame for Checkboxes
        self.checkbox_frame = tk.Frame(master)
        self.checkbox_frame.pack(fill="both", expand=True, padx=10)

        self.canvas = tk.Canvas(self.checkbox_frame)
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

         # Logging Pane on the right
        self.log_frame = tk.Frame(master)
        self.log_frame.pack(fill="both", expand=True, padx=10, pady=(10, 0))

        log_label = tk.Label(self.log_frame, text="Logs", font=("Helvetica", 12))
        log_label.pack(pady=5)

        self.log_text = tk.Text(self.log_frame, wrap="word", state="disabled", width=30, height=20)
        self.log_text.pack(fill="both", expand=True)

        # Set up logger
        text_handler = TextHandler(self.log_text)
        self.logger.addHandler(text_handler)

    def get_recipes(self):
        """Retrieve a list of RecipeMD files from the recipes directory."""
        meal_files = [f for f in os.listdir(self.recipe_dir) if f.endswith(".md")]
        meal_names = []
        for meal_file in meal_files:
            meal_fp = os.path.join(".", "recipes", meal_file)
            meal_name = subprocess.run(
                ["recipemd", meal_fp, "-t"],
                capture_output=True,
                text=True
            ).stdout
            meal_names.append((meal_file, meal_name.strip()))

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

class TextHandler(logging.Handler):
    """Custom logging handler that outputs log messages to a Tkinter Text widget."""
    def __init__(self, text_widget):
        super().__init__()
        self.text_widget = text_widget

    def emit(self, record):
        log_entry = self.format(record)
        self.text_widget.configure(state="normal")
        self.text_widget.insert(tk.END, log_entry + "\n")
        self.text_widget.configure(state="disabled")
        self.text_widget.yview(tk.END)  # Scroll to the end of the text widget


class ProcessSelection:
    def __init__(self, conf, printer_name):
        self.conf = conf
        self.printer_name = printer_name

    def execute(self, selected_recipes, output_filename):
        meal_fps = [os.path.join(".", "recipes", recipe) for recipe in selected_recipes]
        (meals, items) = self._select_meals(meal_fps)
        logger.info(f"Using meals: {json.dumps(meals)}")
        logger.info(f"Produced ingredient deck: {json.dumps(items)}")

        self._create_latex_document(meals, items, logger=logger)
        self._generate_latex_file(logger=logger)
        self._print_pdf(output_filename, self.printer_name, dry_run=self.conf.dry_run, logger=logger)
        logger.info("Exiting program...\n\n")


    def _select_meals(self, meal_fps, logger=None):
        """
        meal_fps: A collection of `os.path.join(".", "recipes", ".......")`
        """

        meal_names = []
        for meal_fp in meal_fps:
            meal_name = subprocess.run(
                ["recipemd", meal_fp, "-t"],
                capture_output=True,
                text=True
            ).stdout


            meal_names.append(meal_name.replace("\n", ""))


        ingredients = []

        for meal_fp in meal_fps:
            meal_ingredients = subprocess.run(
                ["recipemd", meal_fp, "-i"],
                capture_output=True,
                text=True
            ).stdout

            for mi in meal_ingredients.split("\n"):
                if re.search(r"^to taste", mi) is not None:
                    # Don't print out common ingredients like salt pepper, etc.
                    # Can make this configurable in the future if we want.
                    continue

                if self._in_reject_list(mi):
                    continue

                cleaned_ingredient = re.sub(CLEAN_INGREDIENT_PTN, "", mi).strip()
                ingredients.append(cleaned_ingredient)

        sorted_unique_ingredients = sorted(set(ingredients))
        return (meal_names, sorted_unique_ingredients)

    def _in_reject_list(self, ingredient):
        REJECT_LIST = [r".*water.*"] # Things to omit from a shopping list
        if ingredient.strip() == "":
            return True

        for r in REJECT_LIST:
            if re.search(r, ingredient) is not None:
                return True

        return False


    def _create_latex_document(self, meals, items, logger=None):
        logger.info("Creating generated-list.tex using template.tex")
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template(os.path.join(".", "files", "template.tex"))
        data = { 'items': items, 'meals': meals }
        filled_template = template.render(data)

        with open(os.path.join(".", "files", "generated-list.tex"), "w") as f:
            f.write(filled_template)

    def _generate_latex_file(self, logger=None):
        logger.info("Generating latex file")
        file_path = os.path.join(".", "files", "generated-list.tex")
        file_dir = os.path.join(".", "files")
        subprocess.run(["pdflatex", f"-output-directory={file_dir}", file_path], check=True)

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
