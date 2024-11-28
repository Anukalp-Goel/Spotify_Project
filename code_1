## to get the token

import requests

# Define the URL
url = "https://accounts.spotify.com/api/token"

# Define the headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Define the data
data = {
    "grant_type": "client_credentials",
    "client_id": "__",
    "client_secret": "__"
}

# Make the POST request
response = requests.post(url, headers=headers, data=data)

#Store the token
token = response.json()

# Print the response
print("Status Code:", response.status_code)
print("Response JSON:", token)


## to get the data

# Define the URL
artist_id = input()
artists_url = f"https://api.spotify.com/v1/artists/{artist_id}"

# Define the headers with the Authorization Bearer token
headers = {
    "Authorization" : f"Bearer {token['access_token']}'"
}

# Make the GET request
response = requests.get(artists_url, headers=headers)

# Print the response
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
