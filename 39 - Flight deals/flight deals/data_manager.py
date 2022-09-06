import requests
import keys

SHEET_API_KEY = keys.SHEET_API_KEY
headers = {
    "Authorization": SHEET_API_KEY
}
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/6029f5fc85dd67642a2a97a834373e07/flightDeals/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                headers=headers,
                json=new_data
            )
            print(response.text)
