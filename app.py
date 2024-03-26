import spotipy
from spotipy.oauth2 import SpotifyOAuth

def get_matching_artists(artists, liked_songs):
    matching_artists = {}
    for song in liked_songs['items']:
        track_artists = [artist['name'] for artist in song['track']['artists']]
        for artist in artists:
            if artist in track_artists:
                if artist not in matching_artists:
                    matching_artists[artist] = {'songs': [], 'count': 0}
                matching_artists[artist]['songs'].append(song['track']['name'])
                matching_artists[artist]['count'] += 1
                break
    return matching_artists

# Recursively call Spotify API to get all user's liked songs
def get_liked_songs_from_spotify(sp, offset=0, limit=50):
    liked_songs = sp.current_user_saved_tracks(offset=offset, limit=limit)
    print(f"Retrieved {offset + len(liked_songs['items'])} songs...", end="\r")
    if liked_songs['next']:
        liked_songs['items'].extend(get_liked_songs_from_spotify(sp, offset=offset+limit, limit=limit)['items'])
    return liked_songs

def get_liked_songs(sp):
    # Check if liked songs are already saved in cache file
    try:
        with open("liked_songs.txt", "r") as f:
            # Ask if user wants to update their list of liked songs
            update = input("Would you like to update your list of liked songs? (y/n) ")
            if update.lower() == 'y':
                raise FileNotFoundError

            # Read liked songs from file
            liked_songs = {'items': [{'track': {'name': line.split(' by ')[0], 'artists': [{'name': line.split(' by ')[1].strip()}]}} for line in f.readlines()]}
    except FileNotFoundError:
        liked_songs = get_liked_songs_from_spotify(sp)

        print()
        print()

        # Save liked songs to a file (overwrite if it already exists)
        with open("liked_songs.txt", "w") as f:
            for song in liked_songs['items']:
                f.write(f"{song['track']['name']} by {song['track']['artists'][0]['name']}\n")
    return liked_songs

def main():
    # User Input: List of artists
    artists = input("Enter a comma-separated list of artists: ").split(',')

    # Spotify authentication and authorization
    scope = "user-library-read"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

    # Get user's liked songs
    liked_songs = get_liked_songs(sp)

    # Find matching artists
    matching_artists = get_matching_artists(artists, liked_songs)

    if matching_artists:
        print("Matching artists found in your liked songs:")
        for artist, data in matching_artists.items():
            print(f"{artist} ({data['count']} matching songs):")
            for song in data['songs']:
                print(f"- {song}")
    else:
        print("No matching artists found in your liked songs.")

if __name__ == "__main__":
    main()
