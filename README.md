# QuickMeals
QuickMeals is an AI-powered web application that detects ingredients from an image of your fridge or food items and generates possible recipes based on what you have!

Due to heavy AI dependencies (PyTorch + Transformers), this application cannot be reliably deployed on free hosting platforms such as Vercel or Render.
To use QuickMeals, you must run it locally on your machine.

Before running the app, you must install:
- Python 3.9+
- pip
- virtualenv

### Installation steps

#### 1. Clone the repository
Paste:
```bash
git clone [https://github.com/your-username/quickmeals.git](https://github.com/johanz043/QuickMeals.git)
```
in your local terminal (I use windows powershell). Put it into your local files.

#### 2. Create virtual environment
Paste the following into your terminal (this is for windows)
python -m venv venv
.\venv\Scripts\Activate.ps1

#### 3. Install dependencies
pip install -r requirements.txt

#### 4. Run the application
python main.py

The url should appear in the terminal. Just copy and paste it into your web browser.
Should look a bit like this: http://127.0.0.1:5000
