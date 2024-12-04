## to get the token

import requests
from dotenv import load_dotenv
import os # to run load_dotenv

# Define the URL for API token
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
# print("Status Code:", response.status_code)
# print("Response JSON:", response.json())
# print("\n\n")


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

processed_data = [] # a list to hold the processed rows
playlist_id = data['id']
playlist_name = data['name']

for x in data['tracks']['items']:

    # Access the 'track' dictionary
    track = x['track']

    # Extract the required fields
    track_id = track['id']
    track_name = track['name']
    track_duration = track['duration_ms']
    track_popularity = track['popularity']
    album_id = track['album']['id']
    album_name = track['album']['name']
    album_release_date = track['album']['release_date']
    artist_ids = [artist['id'] for artist in track['artists']]

    # Append the data as a dictionary
    processed_data.append({
        'track_id' : track_id,
        'track_name' : track_name,
        'track_duration' : track_duration,
        'track_popularity' : track_popularity,
        'album_id': album_id,
        'album_name': album_name,
        'album_release_date': album_release_date,
        'artist_ids': ", ".join(artist_ids),  # Convert list of artists to a string
    })


# Convert the list of dictionaries into a pandas DataFrame

import pandas as pd
df = pd.DataFrame(processed_data)

# Display the resulting DataFrame
print(df.head())

from sqlalchemy import create_engine

# Define your database connection
connection_string = f"mysql+pymysql://root:{os.getenv('SQL_password')}@localhost/spotify_data"
engine = create_engine(connection_string)

# Export the DataFrame to the SQL database
table_name = "playlist"

# Write the DataFrame to the SQL database
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

print(f"Data successfully exported to the {table_name} table.")

#import the data for all the artists in a artist table for all the artitsts in the playlist tracks
unique_artist_ids = df['artist_ids'].str.split(', ').explode().unique()

## to get the table for artists
processed_artist_data = [] # a list to hold the processed rows
# Define the URL
for artist_id in unique_artist_ids:
    artists_url = f"https://api.spotify.com/v1/artists/{artist_id}"

    # Define the headers with the Authorization Bearer token
    headers = {
        "Authorization" : f"Bearer {token['access_token']}'"
    }

    # Make the GET request
    response = requests.get(artists_url, headers=headers)

    data = response.json()
        
    # Extract the required fields
    id = data['id']
    name = data['name']
    popularity = data['popularity']
    followers = data['followers']['total']

    # Append the data as a dictionary
    processed_artist_data.append({
        'id' : id,
        'name' : name,
        'popularity' : popularity,
        'followers' : followers,
    })


# Convert the list of dictionaries into a pandas DataFrame

df_art = pd.DataFrame(processed_artist_data)

# Display the resulting DataFrame
print(df_art.head())

# Export the DataFrame to the SQL database
table_name = "artist"

# Write the DataFrame to the SQL database
df_art.to_sql(name=table_name, con=engine, if_exists='replace', index=False)

print(f"Data successfully exported to the {table_name} table.")
