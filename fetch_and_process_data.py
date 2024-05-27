import requests
import json
from datetime import datetime

def fetch_and_process_data():
    url = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/master/countries%2Bstates.json"
    response = requests.get(url)
    data = response.json()

    processed_data = []

    for country in data["countries"]:
        country_data = {
            "name": country["name"],
            "states": [{"name": state["name"]} for state in country["states"]]
        }
        processed_data.append(country_data)

    with open("states.json", "w") as f:
        json.dump(processed_data, f, indent=4)

if __name__ == "__main__":
    fetch_and_process_data()
