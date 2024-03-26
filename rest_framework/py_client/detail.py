import requests

#endpoint = "http://localhost:8000/api/"
endpoint = "http://localhost:8000/api/product/view/123" #http://127.0.0.1:8000/

get_response = requests.get(endpoint)

#print(get_response.text)

print(get_response.json())
print(get_response.status_code)


