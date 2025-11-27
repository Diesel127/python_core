import requests

url = 'https://jsonplaceholder.typicode.com/posts'
data = {"name": "Alice", "age": 30}
response = requests.post(url, json=data)
print(response.status_code)
print(response.json())