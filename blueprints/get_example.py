import requests

URL = "https://jsonplaceholder.typicode.com"

response = requests.get(URL + "/todos")

if int(response.status_code//100) != 2:
    print(f"Error: {response.status_code}")
    response.raise_for_status()

todo_list = response.json()

print("Found a total of", len(todo_list), "entries!")