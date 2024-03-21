import requests

#endpoint = "http://localhost:8000/api/"
#endpoint = "http://localhost:8000/get/" #http://127.0.0.1:8000/
endpoint = "http://localhost:8000/post/"

#get_response = requests.get(endpoint, json={"query": "Hello World"})

post_response = requests.post(endpoint, json={'title': 'Juice', 
                                              'content':'Apple', 
                                              'price':'150'})
#print(get_response.text)

# print(get_response.json())
# print(get_response.status_code)

print(post_response.json())
print(post_response.status_code)
