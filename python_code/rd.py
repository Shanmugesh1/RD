import json

service = {
    "id":"1",
    "name": "hotal"
}


with open("service.json", "w") as file:
    json.dump(service, file, indent=4)

print("JSON file created successfully.")


city = {
    "id":"1",
    "name": "ammapattai"
}


with open("city.json", "w") as file:
    json.dump(city, file, indent=4)

print("JSON file created successfully.")


location= {
    "id":"1",
    "name": "krk street"
}


with open("location.json", "w") as file:
    json.dump(location, file, indent=4)

print("JSON file created successfully.")
