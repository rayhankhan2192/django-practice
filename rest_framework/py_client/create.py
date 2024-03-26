import requests

endpoint = "http://localhost:8000/api/product/create/"


data = {
    'title': 'juice',
    'content': 'Mango',
    'price': 200
}

get_response = requests.post(endpoint, json=data)

#print(get_response.text)

print(get_response.json())
print(get_response.status_code)


