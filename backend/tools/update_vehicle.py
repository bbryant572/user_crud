import requests
from pprint import pprint

URL = "http://127.0.0.1:5000/vehicles/"

SAMPLE_VEHICLE = {
    "Make": "Ford",
    "Model": "F250",
    "Color": "Gun Metal"
}


def update_vehicle(vehicle_id):
    SAMPLE_VEHICLE["Make"] = input("Enter a Make")
    SAMPLE_VEHICLE["Model"] = input("Enter a Model")
    SAMPLE_VEHICLE["Color"] = input("Enter Color")
    url = "%s%s" % (URL, vehicle_id)
    response = requests.put(url, json=SAMPLE_VEHICLE)
    if response.status_code == 204:
        print("Vehicle updated.")
    else:
        print("Error while trying to update vehicle")


def get_vehicle():
    vehicle_id = input("Type in the desired vehicle id: ")
    url = "%s%s" % (URL, vehicle_id)
    response = requests.get(url)
    vehicle = {}
    if response.status_code == 200:
        response_json = response.json()
        vehicle = response_json["vehicle"][0]
        print("vehicle: ")
        pprint(vehicle)
    else:
        print("Error while trying to retrive vehicle.")
    return vehicle.get("id")


if __name__ == "__main__":
    print("UPDATE VEHICLE")
    print("-----------")
    vehicle_id = get_vehicle()
    update_vehicle(vehicle_id)
