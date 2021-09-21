import requests
import json
from jsonpath import jsonpath

url = "https://reqres.in/api/users?page=2"
request = requests.get(url)
print(request.text)
status_code = request.status_code
print("status code = "+ str(status_code))

text = json.loads(request.text)
print(text)

x = jsonpath(text,'total')
print(x[0])
y = jsonpath(text,'data[0]')
print(y[0])
for z in text['data']:
    print(z['first_name'])