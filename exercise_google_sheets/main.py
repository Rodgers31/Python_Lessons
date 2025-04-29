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
for values in result['exercises']:
    date = datetime.now()
    final_date = date.strftime("%x")
    time = date.strftime("%X")
    workouts = {
        'workout': {
            'date': final_date,
            'time': time,
            'exercise': values["user_input"],
            'duration': values["duration_min"],
            'calories': values["nf_calories"]
        }
    }
    bearer_headers = {
        "Authorization": "Bearer " + os.getenv("AUTH")
    }
    sheety_end = "https://api.sheety.co/540b1e9afd000ccde8593508ff18f08c/myWorkouts/workouts"
    workout = requests.post(url=sheety_end, headers=bearer_headers, json=workouts)
    result = workout.json()
    print(result)
