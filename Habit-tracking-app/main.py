import requests
from datetime import datetime

pixela_enpoint = "https://pixe.la/v1/users"
TOKEN = "hsusus663829hhsj"
USERNAME = "ibby"

params = {
    "token":TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=pixela_enpoint,json=params)
# print(response.text)
#
headers = {
    "X-USER-TOKEN": TOKEN
}
graph_config = {
    "id": "graph1",
    "name": "coding graph",
    "unit": "hours",
    "type": "float",
    "color":"sora"
}

graph_endpoint = f"{pixela_enpoint}/{USERNAME}/graphs"

# response = requests.post(url=graph_endpoint,json=graph_config,headers=headers)
# print(response.text)

post_endpoint = f"{graph_endpoint}/graph1"

today = datetime.now().strftime("%Y%m%d")

post_config = {
    "date": today,
    "quantity": "5"

}
# response = requests.post(url=post_endpoint,json=post_config,headers=headers)
# print(response.text)


put_config = {
    "quantity": "100"
}

put_endpoint = f"{post_endpoint}/{today}"

response = requests.delete(url=put_endpoint,headers=headers)
print(response.text)