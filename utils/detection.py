from transformers import pipeline # Import Hugging Face pipeline for running pretrained ML models
from PIL import Image # Import PIL (Python Imaging Library) for opening and processing images

# Load a pretrained image classification pipeline
classifier = pipeline(
    "image-classification",
    model="nateraw/food" # Uses a food recognition model
)

# Detects foods using the pretrained model then returns a list of ingredients
def detect_food(image_path):

    image = Image.open(image_path) # Open the image from the file path

    results = classifier(image) # Run the image through the classifier model to get results

    ingredients = [] # Stores the ingredients

    for r in results: # Loop through each result returned by the model
        label = r["label"].lower() # Extract the predicted food name and convert to lowercase

        # Clean label by replacing underscores with spaces for readability
        label = label.replace("_", " ")

        ingredients.append(label) # Add cleaned label to the ingredients list

    # Removes duplicate ingredient entries
    ingredients = list(set(ingredients))

    # Return ingredients if any were detected, otherwise return fallback value
    return ingredients if ingredients else ["unknown food"]