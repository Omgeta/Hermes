import json

with open("data/bus_routes.json") as f:
    data = json.load(f)

for key in data[0].keys():
    print(f":{key}, ", end="")
