import requests
from datetime import datetime
import os

GENDER = "YOUR GENDER"
WEIGHT_KG = YOUR WEIGHT
HEIGHT_CM = YOUR HEIGHT
AGE = YOUR AGE


APP_ID = os.environ["APP_ID"]
APP_KEY = os.environ["APP_KEY"]

today = datetime.now()
# Exercise natural language API
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
headers = {
    "x-app-id": APP_ID,
    "x-app-key": APP_KEY,
}

exercise_config = {
    "query": input("Tell me which exercises you did?\n"),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGH_CM,
    "age": AGE,
}
response = requests.post(url=exercise_endpoint, headers=headers, json=exercise_config)
response.raise_for_status()
exercise_data = [exercise for exercise in response.json()['exercises']]

sheety_endpoint = os.environ["SHEET_ENDPOINT"]
sheety_headers = {
    "Authorization": os.environ["SHEET_TOKEN"]
}

for exercise in exercise_data:
    sheety_params = {
        "workout": {
            "date": today.strftime('%d/%m/%Y'),
            "time": today.strftime("%X"),
            "exercise": f"{exercise['name'].title()}",
            "duration": f"{exercise['duration_min']}",
            "calories": f"{exercise['nf_calories']}",
        }
    }
    response = requests.post(url=sheety_endpoint, headers=sheety_headers, json=sheety_params)
