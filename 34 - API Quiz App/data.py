import requests

AMOUNT_OF_QUESTIONS = 10

parameters = {
    "amount": AMOUNT_OF_QUESTIONS,
    "type": "boolean",
    "category": 18,
}
response = requests.get(url="https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
question_data = response.json()["results"]