## to get the token

import requests
from dotenv import load_dotenv
import os

# Define the URL
url = "https://accounts.spotify.com/api/token"

# Define the headers
headers = {
    "Content-Type": "application/x-www-form-urlencoded"
}

# Define the data
load_dotenv()
data = {
    "grant_type": "client_credentials",
    "client_id": f"{os.getenv('client_id')}",
    "client_secret": f"{os.getenv('client_secret')}"
}

# Make the POST request
response = requests.post(url, headers=headers, data=data)

#Store the token
token = response.json()

# Print the response
print("Status Code:", response.status_code)
print("Response JSON:", token)


## to get the sample artist data

# Define the URL
artist_id = f"{os.getenv('artist_id_arijit_singh')}"
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
print("\n\n")


## to get a sample playlist

# Define the URL
playlist_id = f"{os.getenv('playlist_id')}"
playlists_url = f"https://api.spotify.com/v1/playlists/{playlist_id}"

# Define the headers with the Authorization Bearer token
headers = {
    "Authorization" : f"Bearer {token['access_token']}'"
}

# Make the GET request
response = requests.get(playlists_url, headers=headers)

#Store the data
data = response.json()

# Print the response
print("Status Code:", response.status_code)
print("Response JSON:", data['name'])


data2 =  data['tracks']['items']
print(type(data2))


# print(data2[0])

data3 = data2[0]['track']['album']
print(type(data3))

album_id = data2[0]['track']['album']['id']
artists = data2[0]['track']['artists']
name = data2[0]['track']['name']
duration = data2[0]['track']['duration_ms']
popularity = data2[0]['track']['popularity']

print(album_id)
print(artists)
print(name)
print(duration)
print(popularity)

# [print(f"{key}: {value}") for key, value in data.items()]
# url = data['tracks']['href']

# # Define the headers with the Authorization Bearer token
# headers = {
#     "Authorization" : f"Bearer {token['access_token']}'"
# }

# # Make the GET request
# response = requests.get(url, headers=headers)

# # Print the response
# print("Status Code:", response.status_code)
# print("Response JSON:", response.json())

print("\n\n\n\n")