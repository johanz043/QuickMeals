import requests # Import requests to make HTTP API calls
from collections import defaultdict # Import defaultdict to initialize dictionary values

# Function to get full ingredient list for a specific recipe
def get_recipe_ingredients(meal_id):
    url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}" # Fetches detailed meal information by ID
    data = requests.get(url).json()  # Send GET request to API and convert response to JSON

    ingredients = [] #Stores ingredients
    meal = data["meals"][0] # Extract the meal from the response

    for i in range(1, 21): # Loop through possible ingredient fields
        ing = meal.get(f"strIngredient{i}") # Get ingredient value
        if ing and ing.strip(): # Check if ingredient exists and is not empty
            ingredients.append(ing.lower())  # Add ingredient to list

    return ingredients # Return list of ingredients for this recipe


# Function to find recipes based on AI detected ingredients
def get_recipes(ingredients):  # If no ingredients provided, return empty list
    if not ingredients:
        return []

    recipe_matches = defaultdict(int)  # Dictionary to count how many ingredients match each recipe
    recipe_name_map = {} # Dictionary to map meal ID to its name

    for ing in ingredients: # Loop through each detected ingredient
        url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ing}" # Find meals that include this ingredient using TheMealDB API

        try:
            data = requests.get(url).json() # Send GET request and parse JSON response

            if data and data.get("meals"): # Check if API returned valid meals
                for meal in data["meals"]: # Loop through each meal returned for this ingredient
                    meal_id = meal["idMeal"] # Extract unique meal ID
                    meal_name = meal["strMeal"] # Extract meal name

                    recipe_matches[meal_id] += 1 # Increment match count for this meal
                    recipe_name_map[meal_id] = meal_name # Store and update meal name mapping

        except Exception as e: # Catch and print any errors
            print(f"Error for {ing}: {e}")

    if not recipe_matches:  # If no recipes matched any ingredients, return empty list
        return []

    user_ingredients = set(i.lower() for i in ingredients) # Convert user ingredients to lowercase
    results = [] # Initialize list to store final recipe results

    for meal_id, match_count in recipe_matches.items(): # Loop through each matched recipe
        recipe_ings = set(get_recipe_ingredients(meal_id)) # Get full ingredient list for this recipe

        # Append structured result with matching details
        results.append({ 
            "id": meal_id, # Recipe ID
            "name": recipe_name_map[meal_id], # Recipe name
            "match_count": match_count, # Number of matching ingredients
            "matched": list(user_ingredients.intersection(recipe_ings)), # Ingredients user has
            "missing": list(recipe_ings - user_ingredients) # Ingredients user is missing
        })

    results.sort(key=lambda x: x["match_count"], reverse=True) # Sort recipes by highest number of matching ingredients

    return results[:10] # Return top 10 best matching recipes