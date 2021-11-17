# importing the requests library
import requests

# api-endpoint
URL = "http://127.0.0.1:5000/users"

# sending get request and saving the response as response object
request = requests.get(url = URL)

# extracting data in json format
data = request.json()

print(data)
