# recipes.py
import requests
from collections import defaultdict

def get_recipe_ingredients(meal_id):
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
    data = requests.get(url).json()

    ingredients = []
    meal = data["meals"][0]

    for i in range(1, 21):
        ing = meal.get(f"strIngredient{i}")
        if ing and ing.strip():
            ingredients.append(ing.lower())

    return ingredients


def get_recipes(ingredients):
    if not ingredients:
        return []

    recipe_matches = defaultdict(int)
    recipe_name_map = {}

    for ing in ingredients:
        url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ing}"

        try:
            data = requests.get(url).json()

            if data and data.get("meals"):
                for meal in data["meals"]:
                    meal_id = meal["idMeal"]
                    meal_name = meal["strMeal"]

                    recipe_matches[meal_id] += 1
                    recipe_name_map[meal_id] = meal_name

        except Exception as e:
            print(f"Error for {ing}: {e}")

    if not recipe_matches:
        return []

    user_ingredients = set(i.lower() for i in ingredients)
    results = []

    for meal_id, match_count in recipe_matches.items():
        recipe_ings = set(get_recipe_ingredients(meal_id))

        results.append({
            "id": meal_id,
            "name": recipe_name_map[meal_id],
            "match_count": match_count,
            "matched": list(user_ingredients.intersection(recipe_ings)),
            "missing": list(recipe_ings - user_ingredients)
        })

    results.sort(key=lambda x: x["match_count"], reverse=True)

    return results[:10]