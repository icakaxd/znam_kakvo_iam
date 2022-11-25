import json
import requests

url = 'http://ickd.cf/commands.json'
result = requests.get(url)
contents = json.load(result)

print(contents)
