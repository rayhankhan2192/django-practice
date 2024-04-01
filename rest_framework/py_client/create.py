import requests

endpoint = "http://localhost:8000/api/product/create/"

headers = {'Authorization': 'Token 84ca2ee7a1f7e5c503ca17a6a858dc18ac381db0'}

data = {
    'title': 'juice',
    'content': 'Strawbery',
    'price': 300
}

get_response = requests.post(endpoint, json=data, headers=headers)

#print(get_response.text)

print(get_response.json())
print(get_response.status_code)


