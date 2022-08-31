import requests
import constants
from datetime import datetime

# link = https://pixe.la/v1/users/graeme/graphs/graph1.html

USERNAME = constants.USERNAME
USER_TOKEN = constants.USER_TOKEN
GRAPH_ID = "graph1"
TODAY = datetime.now()

# Set Up An Account
pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Set Up A Graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
header = {
    "X-USER-TOKEN": USER_TOKEN
}
graph_config = {
    "id": GRAPH_ID,
    "name": "codegraph",
    "unit": "number",
    "type": "int",
    "color": "kuro",
}

# response = requests.post(url=graph_endpoint, headers=graph_header, json=graph_config)
# print(response.text)

# Post A Value To The Graph
value_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
value_config = {
    "date":f"{TODAY.strftime('%Y%m%d')}",
    "quantity": input("How many minutes did you code for today?\n")
}
response = requests.post(url=value_endpoint, headers=header, json=value_config)
print(response.text)

# Amend Graph
graph_amend_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
graph_amend_config = {
    "unit": "minutes"
}
# response = requests.put(url=graph_amend_endpoint, headers=header, json=graph_amend_config)
# print(response.text)

# Amend Pixel
pixel_amend_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY.strftime('%Y%m%d')}"
pixel_amend_config = {
    "quantity": "75"
}
# response = requests.put(url=pixel_amend_endpoint, headers=header, json=pixel_amend_config)
# print(response.text)