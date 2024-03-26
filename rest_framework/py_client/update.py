import requests

endpoint = "http://localhost:8000/api/product/view/1/update/" 

data = {
    'title': 'Juice',
    'content': 'Mango',
    'price': 100
}

get_response = requests.put(endpoint, json=data)

#print(get_response.text)

#print(get_response.json())
print(get_response.status_code)


