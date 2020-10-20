import json

database = "mini.json"
data = json.loads(open(database).read())

print(data)
