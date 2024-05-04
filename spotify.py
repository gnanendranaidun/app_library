import subprocess

def open_spotify():
    # Path to the Spotify executable file
    spotify_path = r"C:\Users\DSBA\OneDrive\Desktop\Spotify.lnk"  # Update with the actual path
    
    # Open Spotify using subprocess
    subprocess.Popen([spotify_path], shell=True)

if __name__ == "__main__":
    open_spotify()
