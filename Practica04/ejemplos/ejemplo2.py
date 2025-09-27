from fastapi import params
from flask import json
import requests

#r = requests.get("https://jsonplaceholder.typicode.com/todos/1")
#print(r.json())

r = requests.get("https://www.consumerfinance.gov/data-research/consumer-complaints/search/api/v1", params={'size': 10})

r1 = requests.get("https://jsonplaceholder.cypress.io/todos/1")
print(r1.json())
json_response = json.loads(r1.text)
json_response.keys()

r2 = requests.get("https://jsonplaceholder.typicode.com/posts",params={'size':5})
json_response = json.loads(r2.text)


#generar abrir archivo json como objeto de paython
import json

with open('fake_users_data.json', 'r') as file:
    data = json.load(file)

print(data)
# Output: {'name': 'Alice', 'age': 30, 'city': 'New York'}
print(type(data))
# Output: <class 'dict'>

#cargando un archivo json como un diccionario de python
import json

with open("your_data.json", "r") as file:
    data_object = json.load(file)
print(data_object)