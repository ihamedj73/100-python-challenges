import os
import requests
from datetime import datetime

USERNAME = os.getenv("HABIT_TRACKER_USERNAME")
TOKEN = os.getenv("HABIT_TRACKER_TOKEN")
graph_id = os.getenv("HABIT_TRACKER_graph_id")


pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}


# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


graph_config = {
    "id": graph_id,
    "name": "Programming Graph",
    "unit": "hour",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(
#     url=graph_endpoint,
#     json=graph_config,
#     headers=headers
# )

# print(response.text)

today = datetime.now()
formatted_today = today.strftime("%Y%m%d")

create_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}"
pixel_data = {
    "date": formatted_today,
    "quantity": input("How many hours did you spend programming? ")
}


response = requests.post(url=create_pixel_endpoint,
                         json=pixel_data, headers=headers)

print(response.text)

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_id}/{formatted_today}"

pixel_update_data = {
    "quantity": "2"
}

# response = requests.put(
#     url=update_pixel_endpoint,
#     json=pixel_update_data,
#     headers=headers
# )

# print(response.text)

delete_pixel_endpoint = update_pixel_endpoint

# res = requests.delete(url=delete_pixel_endpoint, headers=headers)

# print(res.text)
