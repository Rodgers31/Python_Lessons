import requests
import os
from dotenv import load_dotenv
from pprint import pprint

URL = 'https://api.sheety.co/540b1e9afd000ccde8593508ff18f08c/flightDeals/prices'
load_dotenv('key.env')


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.call_sheet()

    def call_sheet(self):
        bearer_headers = {
            "Authorization": "Bearer " + os.getenv("AUTH")
        }
        response = requests.get(url=URL, headers=bearer_headers)
        return response.json()
