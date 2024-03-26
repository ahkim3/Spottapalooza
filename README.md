# Spottapalooza

Score the Lollapalooza lineup based on your favorite artists on Spotify.

This Python script uses the Spotify API to compare the Lollapalooza lineup with your liked songs on Spotify for each artist performing. The goal is to help you decide which artists to see at Lollapalooza based on your music preferences, as well as what days to attend.

## Requirements

-   Unix-based CLI (Linux, MacOS, etc.)
-   Python 3.X.X
-   Pip X.X.X
-   Spotify account (free or premium)
-   Spotify developer account
-   Spotipy library

## Setup

1. Clone the repository
2. Install the dependencies

```bash
pip install -r requirements.txt
```

3. Create a Spotify app and get the client ID, client secret, and redirect URI
4. Set the client ID and client secret as environment variables

```bash
export SPOTIPY_CLIENT_ID='your_client_id'
export SPOTIPY_CLIENT_SECRET='your_client'
export SPOTIPY_REDIRECT_URI='your_redirect_uri'
```

5. Run the app

```bash
python app.py
```

## Tips

-   The app will open a browser window to authenticate with Spotify
-   The app will save the authentication token in a file called `.cache`
-   -   To reset the authentication token, delete the `.cache` file
-   The app will cache liked songs in a file called `liked_songs.txt`
-   -   To update the liked songs, delete the `liked_songs.txt` file, or select 'y' when prompted in the program
-   The lineup data is stored as a CSV file called `lollapalooza_lineup_2024.csv`. This may be modified as needed.
