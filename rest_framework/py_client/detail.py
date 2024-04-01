import requests
from getpass import getpass
#endpoint = "http://localhost:8000/api/"

auth_endpoint = "http://localhost:8000/api/auth/"

username = input("username: ")
password = getpass("Password: ")

auth_response = requests.post(auth_endpoint,
                              json={'username': username, 'password': password})
print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        "Authorization": f"Token {token}"
    }
    
    endpoint = "http://localhost:8000/api/product/create/" #http://127.0.0.1:8000/

    get_response = requests.get(endpoint, headers=headers)
    print(get_response.json())
    print(get_response.status_code)


