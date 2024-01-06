import requests
from requests.auth import HTTPBasicAuth

def get_json_from_api_with_auth(api_url, username, password):
    try:
        # Make a GET request to the API with authentication
        response = requests.get(api_url, auth=HTTPBasicAuth(username, password))

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON data from the response
            json_data = response.json()
            return json_data
        else:
            # Print an error message if the request was not successful
            print(f"Error: {response.status_code}")
            return None

    except requests.exceptions.RequestException as e:
        # Print an error message if an exception occurs during the request
        print(f"Error: {e}")
        return None

# Example usage:
api_url = "https://example.com/api/data"  # Replace with your API endpoint
username = "your_username"
password = "your_password"

json_data = get_json_from_api_with_auth(api_url, username, password)

if json_data:
    # Print the parsed JSON data
    print(json_data)
