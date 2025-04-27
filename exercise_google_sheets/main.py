import requests
import os
from dotenv import load_dotenv
from datetime import datetime

URL = 'https://trackapi.nutritionix.com'
load_dotenv('key.env')


parameters = {
    'Content-Type': 'application/json',
    'x-app-id': os.getenv("ID"),
    'x-app-key': os.getenv("KEY")
}

exercise = input("Tell me which exercise you did: ")
response = requests.get(url=URL, headers=parameters, params=exercise)