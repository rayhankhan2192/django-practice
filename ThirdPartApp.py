#Acces the data from RESTfulAPI 

import requests


URL = "http://127.0.0.1:8000/arena/details/"

response = requests.get(url=URL)
data = response.json()

print(data)