import requests
import constants

USERNAME = constants.USERNAME
USER_TOKEN = constants.USER_TOKEN

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": USER_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
graph_header = {
    "X-USER-TOKEN": USER_TOKEN
}
graph_config = {
    "id": "graph1",
    "name": "codegraph",
    "unit": "number",
    "type": "int",
    "color": "kuro",
}
# response = requests.post(url=graph_endpoint, headers=graph_header, json=graph_config)
# print(response.text)
