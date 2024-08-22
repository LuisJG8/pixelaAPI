import requests
from datetime import datetime

USERNAME = "YOUR USER"
TOKEN = "YOUR TOKEN"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_configuration = {
    "id": "YOUR ID",
    "name": "cycling",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

requests.post(pixela_endpoint)

headers = {
    "X-USER-TOKEN": TOKEN
}

add_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graphomaewakaton"

today = datetime(year=XXXX, month=X, day=XX)
todayFormated = (today.strftime("%Y%m%d"))
print(todayFormated)

post_a_pixel = {
    "date": todayFormated,
    "quantity": "1",
}

updatePixel = {
    "quantity": "0"
}

update_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/graphomaewakaton/{todayFormated}"

new_response = requests.put(url=update_pixel, json=updatePixel,headers=headers)
print(new_response.text)