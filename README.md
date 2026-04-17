# QuickMeals
QuickMeals is an **AI-powered** web application that detects ingredients from an image of your fridge or food items and generates possible recipes based on what you have!

QuickMeals is a full-stack project that combines **Flask** and **Python** for the backend, enabling a lightweight web application structure. It uses **Hugging Face Transformers** and **PyTorch** for AI-powered food image recognition, allowing the system to detect ingredients from uploaded images. The application integrates **TheMealDB API** to retrieve and generate recipe recommendations based on the detected ingredients, while **HTML**, **CSS**, and **JavaScript** are used to create a clean and interactive user interface for a smooth user experience.


Due to heavy AI dependencies (PyTorch + Transformers), this application cannot be reliably deployed on free hosting platforms such as Vercel or Render.
To use QuickMeals, you must run it locally on your machine.

Before running the app, you must install:
- Python 3.9+
- pip
- virtualenv

## Installation steps

#### 1. Clone the repository
Paste:
```bash
git clone https://github.com/johanz043/QuickMeals.git
```
in your local terminal (I use windows powershell). Put it into your local files.

#### 2. Create virtual environment
Paste the following into your terminal (this is for windows)
```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```
#### 3. Install dependencies
Paste this in your terminal
```bash
pip install -r requirements.txt
```
#### 4. Run the application
```bash
python main.py
```
The url should appear in the terminal. Just copy and paste it into your web browser.
Should look a bit like this: http://127.0.0.1:5000

## Demo Video
[Watch a runthrough](https://www.loom.com/share/6004292c43674d3fa37a1e071ddf8c24)
