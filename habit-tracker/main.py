import requests
from datetime import datetime

USERNAME = "rodgers"
TOKEN = "ncsjfg#%ssnkfbwui3312"
ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",

}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# graph_config = {
#     "id": "graph1",
#     "name": "Conding Streak",
#     "unit": "Hr",
#     "type": "float",
#     "color": "sora"
# }
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

today = datetime.now()

post_pixela = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

# check doc - https://www.w3schools.com/python/python_datetime.asp

add_pixel = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "1"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixela = requests.post(url=post_pixela, json=add_pixel, headers=headers)
print(pixela.text)
