from flask import Flask, render_template, request
import os
from utils.detection import detect_food
from utils.recipes import get_recipes

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
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

            ingredients = detect_food(filepath)
            recipes = get_recipes(ingredients)

    return render_template(
        "index.html",
        image=image,
        ingredients=ingredients,
        recipes=recipes
    )


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)