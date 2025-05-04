import requests
import os
from dotenv import load_dotenv
from pprint import pprint

URL = 'https://api.sheety.co/540b1e9afd000ccde8593508ff18f08c/flightDeals/prices'
load_dotenv('key.env')


class DataManager:
    #This class is responsible for talking to the Google Sheet.

    def __init__(self):
        self.bearer_headers = {
            "Authorization": "Bearer " + os.getenv("AUTH")
        }
        self.destination_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=URL, headers=self.bearer_headers)
        data = response.json()
        self.destination_data = data["prices"]
        # 3. Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # 6. In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{URL}/{city['id']}",
                json=new_data,
                headers=self.bearer_headers
            )
            print('put return', response.text)
