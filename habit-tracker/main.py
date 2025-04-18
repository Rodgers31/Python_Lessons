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

today = datetime(year=2025, month=4, day=14)
post_pixela = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}"

# check doc - https://www.w3schools.com/python/python_datetime.asp
# **post request ***
# add_pixel = {
#     "date": today.strftime("%Y%m%d"),
#     "quantity": "5"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# pixela = requests.post(url=post_pixela, json=add_pixel, headers=headers)
# print(pixela.text)
# update_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today.strftime("%Y%m%d")}"
#
# pixel_data = {
#     "quantity": "2"
# }
#
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#

# response = requests.put(url=update_pixel, json=pixel_data, headers=headers)
# print(response.text)

delete_pixel = f"{pixela_endpoint}/{USERNAME}/graphs/{ID}/{today.strftime("%Y%m%d")}"

header = {
    "X-USER-TOKEN": TOKEN
}
remove = requests.delete(url=delete_pixel, headers=header)
print(remove.text)