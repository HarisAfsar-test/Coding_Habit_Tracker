
import os
import requests
import datetime


#CONSTANTS
USERNAME=os.environ.get("USERNAME")
TOKEN=os.environ.get("TOKEN")
GRAPH_ID="graph1"
API_ENDPOINT="https://pixe.la/v1/users"
GRAPH_ENDPOINT=f"{API_ENDPOINT}/{USERNAME}/graphs"
PIXEL_ENDPOINT=f"{API_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.datetime.now().strftime("%Y%m%d")

pixel_parameters={
    "date":str(today),
    "quantity":input("Please enter the quantity of the coding today: ")


}
parameters={
    "token":os.environ.get("TOKEN"),
    "username":os.environ.get("USERNAME"),
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
graph_parameters={
    "id":"graph1",
    "name":"Coding Habit",
    "description":"Coding Habit",
    "unit":"Lines",
    "type":"int",
    "color":"momiji",
}
headers = {
    "X-USER-TOKEN":TOKEN
}


response = requests.post(url=PIXEL_ENDPOINT, json=pixel_parameters,headers=headers)

response.raise_for_status()
print(response.text)
