import requests

try:
    # Make the API call
    response = requests.get('https://example_site.com/<API_KEY>')
    
    # Raise an exception if the response has an HTTP error
    response.raise_for_status()
    
    # Parse the response JSON
    data = response.json()
    print("Data received:", data)

except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
    raise  # Re-raise the exception if needed for further handling



