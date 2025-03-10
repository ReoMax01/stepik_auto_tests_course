import json

import requests

url = "https://dog.ceo/api/breed/hound/images"

get_request = requests.get(url)
data = get_request.json()
count = sum('hound-english' in img for img in data['message'])
print(count)