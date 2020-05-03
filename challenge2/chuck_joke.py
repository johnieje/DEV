import requests
import json

url = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url)

# String data
data = response.text

# Dictionary data
json_data = json.loads(data)
print(json_data['value'])