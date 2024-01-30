import requests, json

URL = 'http://127.0.0.1:8000/arena/info/'

data = {
    'id': 24,
}

json_data = json.dumps(data)

send = requests.delete(url=URL, data=json_data)

data = send.json()

print(data)