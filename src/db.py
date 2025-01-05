from dataclasses import asdict
import sqlite3
import json
from seeds.recipes import recipe_seeds
from recipe_schema import Recipe


def create_db(db_name="recipes.db"):
    # Connect to the SQLite3 database (creates the file if it doesn't exist)
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create the `recipes` table if it doesn't exist
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS recipes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            ingredients TEXT NOT NULL, -- JSON serialized list of ingredients
            instructions TEXT NOT NULL -- JSON serialized list of instructions
        )
    """
    )
    conn.commit()
    conn.close()


def add_recipe(recipe: Recipe, db_name: str = "recipes.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Insert the recipe into the table
    cursor.execute(
        """
        INSERT INTO recipes (title, description, ingredients, instructions)
        VALUES (?, ?, ?, ?)
    """,
        (
            recipe.title,
            recipe.description,
            json.dumps([asdict(ingredient) for ingredient in recipe.ingredients]),
            json.dumps(recipe.instructions),
        ),
    )
    conn.commit()
    conn.close()


def get_all_recipes(db_name: str = "recipes.db"):
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM recipes")
    rows = cursor.fetchall()
    recipes = []
    for row in rows:
        recipes.append(
            {
                "id": row[0],
                "title": row[1],
                "description": row[2],
                "ingredients": json.loads(row[3]),
                "instructions": json.loads(row[4]),
            }
        )
    conn.close()
    return recipes


def seed_recipes():
    [add_recipe(recipe) for recipe in recipe_seeds]
