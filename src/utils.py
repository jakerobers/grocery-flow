from typing import Self
import subprocess
import os
import re


def create_latex_document(template, tex_path, meals, all_ingredients, logger):
    logger.info("Creating generated-list.tex using template.tex")

    rendered_meals = []
    for meal in meals:
        rendered_meals.append(f"({meal['short_code']}) {meal['title']}")

    items = []
    for ingredient in all_ingredients:
        tags = ", ".join(ingredient["tags"])
        if len(ingredient["quantities"]) > 0:
            quantities = ", ".join(ingredient["quantities"])
            quantities = f" ({quantities})"
        else:
            quantities = ""

        items.append(f"{ingredient['name']}{quantities} ({tags})")

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
                quantity = None
                if meal_ingredient["quantity"]:
                    quantity = f"{round(meal_ingredient['quantity'], 2)} {meal_ingredient['unit']}"

                found = False
                i = 0
                while not found and i < len(all_ingredients):
                    if all_ingredients[i]["name"] == meal_ingredient["name"]:
                        found = True
                        all_ingredients[i]["tags"].append(meal["short_code"])
                        if quantity:
                            all_ingredients[i]["quantities"].append(quantity)
                    i += 1

                if not found:
                    quantities = []
                    if quantity:
                        quantities = [quantity]

                    all_ingredients.append(
                        {
                            "name": meal_ingredient["name"],
                            "tags": [meal["short_code"]],
                            "quantities": quantities,
                        }
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
