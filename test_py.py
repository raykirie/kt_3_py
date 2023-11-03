import requests 

base_url = "https://example.com/api/" 

response_user = requests.get(base_url + "user")
print("GET запрос к /user:", response_user.text)

data = {"username": "new_user", "email": "user@example.com"}
response_post_user = requests.post(base_url + "user", json=data)
print("POST запрос к /user:", response_post_user.text)

response_store = requests.get(base_url + "store")
print("GET запрос к /store:", response_store.text)

store_data = {"name": "New Store"}
response_put_store = requests.put(base_url + "store/1", json=store_data)
print("PUT запрос к /store/1:", response_put_store.text)
