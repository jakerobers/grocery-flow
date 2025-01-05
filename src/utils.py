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


def create_latex_document(template, tex_path, meals, all_ingredients, logger):
    logger.info("Creating generated-list.tex using template.tex")

    rendered_meals = []
    for meal in meals:
        rendered_meals.append(f"({meal['short_code']}) {meal['title']}")

    items = []
    for ingredient in all_ingredients:
        tags = ", ".join(ingredient["tags"])
        items.append(f"{ingredient['name']} ({tags})")

    data = {"items": items, "meals": rendered_meals}
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
    def select_meals(self, recipes, logger=None):
        """
        meal_fps: A collection of `os.path.join(".", "recipes", ".......")`
        """

        meals = []
        letter = 65  # A

        for recipe in recipes:
            recipe_ingredients = []
            for ingredient in recipe["ingredients"]:
                if re.search(r"^to taste", ingredient["name"]) is not None:
                    # Don't print out common ingredients like salt pepper, etc.
                    # Can make this configurable in the future if we want.
                    continue

                if self._in_reject_list(ingredient["name"]):
                    continue

                recipe_ingredients.append(ingredient)

            meals.append(
                {
                    "title": recipe["title"],
                    "short_code": chr(letter),
                    "ingredients": recipe_ingredients,
                }
            )
            letter += 1

        all_ingredients = []
        for meal in meals:
            for meal_ingredient in meal["ingredients"]:
                found = False
                i = 0
                while not found and i < len(all_ingredients):
                    if all_ingredients[i]["name"] == meal_ingredient["name"]:
                        found = True
                        all_ingredients[i]["tags"].append(meal["short_code"])
                        # TODO: add the quantities together
                    i += 1

                if not found:
                    all_ingredients.append(
                        {"name": meal_ingredient["name"], "tags": [meal["short_code"]]}
                    )

        return (meals, all_ingredients)

    def _in_reject_list(self, ingredient):
        REJECT_LIST = [r".*water.*"]  # Things to omit from a shopping list
        if ingredient.strip() == "":
            return True

        for r in REJECT_LIST:
            if re.search(r, ingredient) is not None:
                return True

        return False
