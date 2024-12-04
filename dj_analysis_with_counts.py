import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from collections import Counter

# Spotify API scopes for reading and writing playlists
SCOPES = "playlist-modify-public playlist-read-private playlist-read-collaborative"

def authenticate_spotify():
    """Authenticate with Spotify API."""
    return spotipy.Spotify(auth_manager=SpotifyOAuth(scope=SCOPES))

def get_tracks_from_playlists(sp, playlist_uris):
    """Extract all tracks from the provided playlists."""
    all_tracks = []
    for uri in playlist_uris:
        playlist_id = uri.split(":")[-1]
        results = sp.playlist_tracks(playlist_id)
        tracks = results["items"]
        while results["next"]:
            results = sp.next(results)
            tracks.extend(results["items"])
        all_tracks.extend([track["track"]["id"] for track in tracks if track["track"]])
    return all_tracks

def create_top_100_playlist(sp, dj_name, track_counts):
    """Create a new playlist with the top 100 most played songs."""
    # Generate playlist title
    playlist_title = f"DJ {dj_name}'s 2024 Top 100 Songs"
    user_id = sp.me()["id"]
    
    # Create a new playlist
    playlist = sp.user_playlist_create(
        user=user_id,
        name=playlist_title,
        public=True,
        description="Top 100 songs played during DJ sets in 2024"
    )
    
    # Get the top 100 unique tracks
    top_100_tracks = [track for track, _ in track_counts.most_common(100)]
    
    # Add tracks to the new playlist
    sp.playlist_add_items(playlist_id=playlist["id"], items=top_100_tracks)

    return playlist["external_urls"]["spotify"]

def main():
    # Authenticate Spotify
    sp = authenticate_spotify()
    
    # Get the DJ's name
    dj_name = input("Enter the DJ's name: ").strip()
    if not dj_name:
        print("DJ name cannot be empty.")
        return
    
    # Get the file path containing playlist URIs
    file_path = input("Enter the path to the file containing playlist URIs: ").strip()
    if not os.path.exists(file_path):
        print("File not found. Please provide a valid file path.")
        return
    
    # Read playlist URIs from the file
    with open(file_path, "r") as f:
        playlist_uris = [line.strip() for line in f if line.strip()]
    
    if not playlist_uris:
        print("No playlist URIs found in the file.")
        return
    
    # Get all tracks from the playlists
    print("Fetching tracks from playlists...")
    all_tracks = get_tracks_from_playlists(sp, playlist_uris)
    if not all_tracks:
        print("No tracks found in the provided playlists.")
        return
    
    # Count the occurrences of each track
    track_counts = Counter(all_tracks)
    
    # Create a new playlist with the top 100 tracks
    print("Creating the top 100 playlist...")
    playlist_url = create_top_100_playlist(sp, dj_name, track_counts)
    
    # Display results
    print(f"Playlist created successfully: {playlist_url}")
    print("Top 100 Songs:")
    for track_id, count in track_counts.most_common(100):
        track = sp.track(track_id)
        print(f"{track['name']} by {', '.join(artist['name'] for artist in track['artists'])} - Played {count} times")

if __name__ == "__main__":
    main()
