import requests

endpoint = "http://localhost:8000/api/product/view/1/delete/" 


get_response = requests.delete(endpoint)

#print(get_response.text)

#print(get_response.json())
print(get_response.status_code)


