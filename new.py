import tkinter as tk
from PIL import Image, ImageTk  # Import PIL for image resizing
import subprocess

def open_microsoft_edge():
    subprocess.Popen(["C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"])

def open_spotify():
    # Path to the Spotify executable file
    spotify_path = r"C:\Users\DSBA\AppData\Local\Microsoft\WindowsApps\spotify.exe"  # Update with the actual path
    
    # Open Spotify using subprocess
    subprocess.Popen([spotify_path], shell=True)

def open_store():
    store_path = r"C:\Users\DSBA\OneDrive\Desktop\Microsoft Store.lnk"
    subprocess.Popen([store_path], shell=True)

def main():
    # Create a Tkinter root widget
    root = tk.Tk()
    # Set the dimensions of the window
    window_width = 1000
    window_height = 650
    
    # Get the screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    
    # Calculate the position for the window to be centered on the screen
    x = (screen_width - window_width) // 10
    y = (screen_height - window_height) // 10
    
    # Set the geometry of the window
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # Set the title of the window
    root.title("Dashboard")
    
    # Load the icon image
    icon_path = "C:/Users/DSBA/Downloads/icon.png"
    icon_image = Image.open(icon_path)
    
    # Resize the icon image to fit the desired dimensions
    icon_image = icon_image.resize((80, 80))
    
    # Convert the resized image to a format compatible with Tkinter
    icon_photo = ImageTk.PhotoImage(icon_image)
    
    # Create a button for Microsoft Edge
    edge_button = tk.Button(root, text="Microsoft Edge", image=icon_photo, compound=tk.TOP, command=open_microsoft_edge)
    edge_button.pack(side=tk.LEFT, padx=10, pady=10)
    
    # Load the Spotify icon image
    spotify_icon_path = "c:\\Users\\DSBA\\Downloads\\spotify_icon.png"  # Replace with the actual path to the Spotify icon
    spotify_icon_image = Image.open(spotify_icon_path)
    
    # Resize the Spotify icon image to fit the desired dimensions
    spotify_icon_image = spotify_icon_image.resize((80, 80))
    
    # Convert the resized image to a format compatible with Tkinter
    spotify_icon_photo = ImageTk.PhotoImage(spotify_icon_image)
    
    # Create a button for Spotify
    spotify_button = tk.Button(root, text="Spotify", image=spotify_icon_photo, compound=tk.TOP, command=open_spotify)
    spotify_button.pack(side=tk.RIGHT, padx=10, pady=10)

    # Load the store icon image
    store_icon_path = "c:\\Users\\DSBA\\Downloads\\store_icon.png"  # Replace with the actual path to the store icon
    store_icon_image = Image.open(store_icon_path)
    
    # Resize the store icon image to fit the desired dimensions
    store_icon_image = store_icon_image.resize((80, 80))
    
    # Convert the resized image to a format compatible with Tkinter
    store_icon_photo = ImageTk.PhotoImage(store_icon_image)
    
    # Create a button for the Microsoft Store
    store_button = tk.Button(root, text="Microsoft Store", image=store_icon_photo, compound=tk.TOP, command=open_store)
    store_button.pack(side=tk.LEFT, padx=10, pady=10)

    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
