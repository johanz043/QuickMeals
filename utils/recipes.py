# recipes.py
import requests
from collections import defaultdict

def get_recipes(ingredients):
    if not ingredients:
        return ["No ingredients detected 😢"]

    recipe_matches = defaultdict(int)
    recipe_name_map = {}

    for ing in ingredients:
        url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ing}"

        try:
            response = requests.get(url)
            data = response.json()

            if data and data.get("meals"):
                for meal in data["meals"]:
                    meal_id = meal["idMeal"]
                    meal_name = meal["strMeal"]

                    recipe_matches[meal_id] += 1
                    recipe_name_map[meal_id] = meal_name

        except Exception as e:
            print(f"Error for {ing}: {e}")

    if not recipe_matches:
        return ["No recipes found 😢"]

    sorted_recipes = sorted(recipe_matches.items(), key=lambda x: x[1], reverse=True)

    return [recipe_name_map[r[0]] for r in sorted_recipes][:10]