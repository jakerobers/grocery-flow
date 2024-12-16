from typing import Self
import subprocess
import os
import re

CLEAN_INGREDIENT_PTN = r"^(to taste|to serve|[\d]+(?:\.\d+)?(?:\s(?:diced|oz|cups?|cloves?|grams?|teaspoons?|pinches?|packages?|tablespoons?|sliced|grated|ground|melted|ounces|lb|minced|tbsp|tsp|bunch|chopped|halved|scoop|juiced|pounds|stalks?|pinch|cans?|squeezed))*)\s*"

# TODO: make this configurable from the UI
PINNED_RECIPES = ["bean_stuff.md", "mexican_quinoa.md"]


def get_printer_name(logger=None):
    # printer {{name}} is idle.  enabled since {{datetime}}
    lpstat_output = subprocess.run(
        ["lpstat", "-p"], capture_output=True, text=True
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


def get_recipes(recipe_dir, logger):
    """Retrieve a list of RecipeMD files from the recipes directory."""

    PINNED_RECIPES = ["bean_stuff.md", "mexican_quinoa.md"]
    meal_files = [f for f in os.listdir(recipe_dir) if f.endswith(".md")]
    logger.info(f"Found files: {str(meal_files)}")
    pinned_meal_files = [x for x in meal_files if x in PINNED_RECIPES]
    unpinned_meal_files = [x for x in meal_files if x not in PINNED_RECIPES]
    meal_files = pinned_meal_files + unpinned_meal_files

    meal_names = []
    for meal_file in meal_files:
        meal_fp = os.path.join(".", "recipes", meal_file)
        meal_name = subprocess.run(
            ["recipemd", meal_fp, "-t"], capture_output=True, text=True
        ).stdout

        meal_name = meal_name.strip()
        if meal_file in pinned_meal_files:
            meal_name = f"^ {meal_name}"

        meal_names.append((meal_file, meal_name))

    return meal_names


def create_latex_document(template, tex_path, meal_idx, items, logger):
    logger.info("Creating generated-list.tex using template.tex")

    meals = []
    for _k, v in meal_idx.items():
        meals.append(f"({v['short_code']}) {v['title']}")

    data = {"items": items, "meals": meals}
    filled_template = template.render(data)
    with open(tex_path, "w") as f:
        f.write(filled_template)


def generate_pdf(tex_filepath, logger):
    logger.info("Generating latex file")
    directory = os.path.dirname(tex_filepath)
    subprocess.run(
        ["pdflatex", f"-output-directory={directory}", tex_filepath],
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    filename = tex_filepath.split(".")[0]
    filename += ".pdf"
    return os.path.join(directory, filename)


class MealBuilder:
    def __init__(self: Self):
        pass

    def select_meals(self, meal_fps, logger=None):
        """
        meal_fps: A collection of `os.path.join(".", "recipes", ".......")`
        """

        meal_idx = {}
        letter = 65  # A
        for meal_fp in meal_fps:
            meal_name = subprocess.run(
                ["recipemd", meal_fp, "-t"], capture_output=True, text=True
            ).stdout

            meal_title = meal_name.replace("\n", "")
            meal_idx[meal_fp] = {
                "title": meal_title,
                "short_code": chr(letter),
                "ingredients": [],
            }
            letter += 1

        ingredients = []

        for meal_fp in meal_fps:
            meal_ingredients = subprocess.run(
                ["recipemd", meal_fp, "-i"], capture_output=True, text=True
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
                meal_idx[meal_fp]["ingredients"].append(cleaned_ingredient)
                ingredients.append(cleaned_ingredient)

        sorted_unique_ingredients = list(sorted(set(ingredients)))

        # Go through and tag each ingredient to its corresponding meals.
        # This way when you're looking at the shopping list, you can easily
        # tell from a glance which ingredient corresponds to which meal(s)
        tagged_ingredients = []
        for i in sorted_unique_ingredients:
            meal_tag = []

            for _k, v in meal_idx.items():
                if i in v["ingredients"]:
                    meal_tag.append(v["short_code"])

            tagged_ingredients.append(f"{i} ({','.join(meal_tag)})")

        return (meal_idx, tagged_ingredients)

    def _in_reject_list(self, ingredient):
        REJECT_LIST = [r".*water.*"]  # Things to omit from a shopping list
        if ingredient.strip() == "":
            return True

        for r in REJECT_LIST:
            if re.search(r, ingredient) is not None:
                return True

        return False
