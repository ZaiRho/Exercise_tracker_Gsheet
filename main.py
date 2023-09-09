import requests
from datetime import datetime

APP_ID = "88684c37"
API_KEYS = "5c118f84e3f5645a02684c9478beb948"
SHEETY_POST = "https://api.sheety.co/58f8c08ad8e102d36ca6e39a3ebd2936/myWorkouts/workouts"
POST_END_POINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

bearer_headers = {
    "Authorization": "Bearer thisIsSecret1234554321"
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEYS,

}
exercises = input("Tell me what exercises you did? ")
query = dict(query=exercises, gender="male", weight_kg=72.5, height_cm=167.64, age=30)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

response = requests.post(url=POST_END_POINT, json=query, headers=headers)
response.raise_for_status()
data = response.json()
data_extract = data["exercises"]
for i in range(len(data_extract)):
    new_exercise = (data_extract[i]["user_input"])
    new_duration = (data_extract[i]["duration_min"])
    new_calories = (data_extract[i]["nf_calories"])
    add_json = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": new_exercise.title(),
            "duration": new_duration,
            "calories": new_calories
        }}
    response = requests.post(url=SHEETY_POST, json=add_json, headers=bearer_headers)
    response.raise_for_status()



