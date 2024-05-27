import requests
import json

def fetch_and_process_data():
    url = "https://raw.githubusercontent.com/dr5hn/countries-states-cities-database/master/countries%2Bstates.json"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        data = response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return
    
    processed_data = []
    for country in data:
        country_data = {
            "name": country["name"],
            "states": [{"name": state["name"]} for state in country["states"]]
        }
        processed_data.append(country_data)

    try:
        with open("states.json", "w") as f:
            json.dump(processed_data, f, indent=4)
    except IOError as e:
        print(f"Error writing file: {e}")

if __name__ == "__main__":
    fetch_and_process_data()
