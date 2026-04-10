# main.py
from flask import Flask, render_template, request
import os
from utils.detection import detect_food       # call the detection function
from utils.recipes import get_recipes         # call the recipe function

app = Flask(__name__)
UPLOAD_FOLDER = "static/uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def index():
    image = None
    ingredients = []
    recipes = []

    if request.method == "POST":
        file = request.files.get("image")
        if file:
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(filepath)
            image = filepath

            # Detect ingredients
            ingredients = detect_food(filepath)

            # Get recipes
            recipes = get_recipes(ingredients)

    return render_template("index.html",
                           image=image,
                           ingredients=ingredients,
                           recipes=recipes)

if __name__ == "__main__":
    app.run(debug=True)