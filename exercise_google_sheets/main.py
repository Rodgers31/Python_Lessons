import requests
import os
from dotenv import load_dotenv
from datetime import datetime
GENDER = 'male'
WEIGHT_KG = '200'
HEIGHT_CM = '175'
AGE = '26'

URL = 'https://trackapi.nutritionix.com/v2/natural/exercise'
load_dotenv('key.env')

exercise = input("Tell me which exercise you did: ")


headers = {
    'Content-Type': 'application/json',
    'x-app-id': os.getenv("ID"),
    'x-app-key': os.getenv("KEY")
}

parameters = {
    'query': exercise
}


response = requests.post(url=URL, json=parameters, headers=headers)
result = response.json()
print(result)