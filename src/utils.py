import subprocess
import os
import re

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

def get_recipes(recipe_dir):
    """Retrieve a list of RecipeMD files from the recipes directory."""

    PINNED_RECIPES = [
        "bean_stuff.md",
        "mexican_quinoa.md"
    ]
    meal_files = [f for f in os.listdir(recipe_dir) if f.endswith(".md")]
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
