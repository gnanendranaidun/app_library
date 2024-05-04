import tkinter as tk

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
    x = (screen_width - window_width) // 2
    y = (screen_height - window_height) // 2
    
    # Set the geometry of the window
    root.geometry(f"{window_width}x{window_height}+{x}+{y}")
    
    # Set the title of the window
    root.title("Dashboard")
    
    # Run the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    main()
