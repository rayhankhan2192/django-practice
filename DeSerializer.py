import requests, json

#API access on ThirtPartyApps
#Insert to Database

URL = 'http://127.0.0.1:8000/arena/info/'

data = {
    'techer_name': 'Rayhan Khan',
    'course_name': 'Python',
    'course_duration': 6
}

#python data convert to json formate
json_data = json.dumps(data)

send = requests.post(url=URL, data=json_data)

data = send.json()
print(data)