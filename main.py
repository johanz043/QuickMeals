from flask import Flask, render_template, request # Import Flask framework and required functions
import os # Import OS module for handling file paths
from utils.detection import detect_food # Imports detect_food function from detection.py
from utils.recipes import get_recipes # Imports get_recipe function from recipes.py

app = Flask(__name__) # Create a Flask web application instance

UPLOAD_FOLDER = "static/uploads" # This folder stores all the uploaded images
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER # The Flask app uses the folder path


@app.route("/", methods=["GET", "POST"]) # Defines main route, it accepts both GET and POST requests
def index():
    image = None # Stores path of uploaded image
    ingredients = [] # Stores detected ingredients from image
    recipes = [] # Stores generated recipes based on ingredients

    if request.method == "POST": # Check if the request method is POST when a photo is uploaded
        file = request.files.get("image") # Get the uploaded file

        if file: # Ensures a file was actually uploaded
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename) # Create file path in the upload folder
            file.save(filepath) # Save the uploaded file to the server

            image = filepath # Store image path

            # Run AI model to detect ingredients from the uploaded image
            ingredients = detect_food(filepath)

            # Use detected ingredients to fetch matching recipes
            recipes = get_recipes(ingredients)

    # Returns the HTML page with image, ingredients, and recipes data
    return render_template(
        "index.html",
        image=image,
        ingredients=ingredients,
        recipes=recipes
    )


if __name__ == "__main__": # Runs the Flask application
    app.run(debug=True)