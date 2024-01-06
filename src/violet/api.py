import requests

def get_json_from_api(api_url):
    try:
        # Make a GET request to the API
        response = requests.get(api_url)

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
api_url = "https://jsonplaceholder.typicode.com/todos/1"  # Replace with your API endpoint
json_data = get_json_from_api(api_url)

if json_data:
    # Print the parsed JSON data
    print(json_data)

