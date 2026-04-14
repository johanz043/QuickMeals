# utils/detection.py
from transformers import pipeline
from PIL import Image

# Load free food classifier (downloads once, then cached)
classifier = pipeline(
    "image-classification",
    model="nateraw/food"
)

def detect_food(image_path):
    """
    Detect food items using a pretrained Food-101 model.
    Returns a cleaned list of ingredients.
    """

    image = Image.open(image_path)

    results = classifier(image)

    ingredients = []

    for r in results:
        label = r["label"].lower()

        # clean label (Food-101 sometimes returns messy names)
        label = label.replace("_", " ")

        ingredients.append(label)

    # remove duplicates
    ingredients = list(set(ingredients))

    return ingredients if ingredients else ["unknown food"]