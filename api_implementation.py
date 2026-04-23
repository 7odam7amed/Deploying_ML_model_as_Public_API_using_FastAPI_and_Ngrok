import json
import requests

url = 'https://praying-monitor-leverage.ngrok-free.dev/diabetes_prediction'



input_data_for_model = {
    'Pragnencies' : 6, 
    'Glucose' : 148,
    'BloodPressure' : 72, 
    'SkinThickness' : 35,
    'Insulin' : 0,
    'BMI' : 33.6,
    'DiabetesPedigreeFunction' : 0.627,
    'Age' : 50
}


response = requests.post(url, json=input_data_for_model)

print(response.text)