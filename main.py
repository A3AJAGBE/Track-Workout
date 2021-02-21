import requests
import os
from datetime import datetime
from dotenv import load_dotenv
load_dotenv()

current_datetime = datetime.now()
date = current_datetime.strftime("%x")
time = current_datetime.strftime("%X")
print(date, time)


# ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
#
# HEADERS = {
#     "x-app-id": os.environ.get('APP_ID'),
#     "x-app-key": os.environ.get('API_KEY'),
# }
#
# exercise_info = input("What exercise(s) did you complete: ")
#
# PARAMETERS = {
#     "query": exercise_info,
#     "gender": os.environ.get('GENDER'),
#     "weight_kg": os.environ.get('WEIGHT_KG'),
#     "height_cm": os.environ.get('HEIGHT_CM'),
#     "age": os.environ.get('AGE')
# }
#
# response = requests.post(ENDPOINT, json=PARAMETERS, headers=HEADERS)
# result = response.json()
# print(result)
