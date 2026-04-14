# utils/detection.py (YOLOv8)
from transformers import pipeline
from PIL import Image

classifier = None

def get_classifier():
    global classifier
    if classifier is None:
        print("Loading food classifier...")
        classifier = pipeline(
            "image-classification",
            model="nateraw/food"
        )
    return classifier


def detect_food(image_path):
    """
    Detect food items using a pretrained Food-101 model.
    Returns a cleaned list of ingredients.
    """

    clf = get_classifier()

    image = Image.open(image_path)
    results = clf(image)

    ingredients = []

    for r in results:
        label = r["label"].lower()
        label = label.replace("_", " ")
        ingredients.append(label)

    ingredients = list(set(ingredients))

    return ingredients if ingredients else ["unknown food"]