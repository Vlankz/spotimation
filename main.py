import os

def open_spotify():
    
    spotify_path = r"C:\Users\User\AppData\Roaming\Spotify\Spotify.exe"  #change the file path if necessary

    if os.path.exists(spotify_path):
        try:
            os.system(f'"{spotify_path}"')
        except Exception as e:
            print(f"Error opening Spotify: {e}")
    else:
        print("Spotify not found. Please check the path to your Spotify executable.")

if __name__ == "__main__":
    open_spotify()
