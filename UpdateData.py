import requests, json

#API access on ThirtPartyApps

URL = 'http://127.0.0.1:8000/arena/info/'

data = {
    'id': 25,
    # 'techer_name': 'Md Rayhan Khan',
     'course_name': 'Networking',
    'course_duration': 6
}

json_data = json.dumps(data)

send = requests.put(url = URL, data=json_data)
msg = send.json()
print(msg)