import requests


URL = "http://127.0.0.1:5000/vehicles/"

SAMPLE_VEHICLE = {
    "Make": "Ford",
    "Model": "F250",
    "Color": "Gun Metal",
}


def create_vehicle():
    Make = input("Enter a Make: ")
    Model = input("Enter a Model: ")
    Color = input("Enter Color: ")
    SAMPLE_VEHICLE["Make"] = Make
    SAMPLE_VEHICLE["Model"] = Model
    SAMPLE_VEHICLE["Color"] = Color
    response = requests.post(URL, json=SAMPLE_VEHICLE)
    if response.status_code == 204:
        print("Vehicle created.")
    else:
        print("Error while attempting to create vehicle.")


if __name__ == "__main__":
    print("CREATE VEHICLE")
    print("------------")
    create_vehicle()
