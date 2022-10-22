import json


with open("./settings.json") as file:
    print(json.load(file))
