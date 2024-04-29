import tkinter as tk
from tkinter import ttk
import pywhatkit as pwk

def play_video():
    video_name = entry_video_name.get()
    singer_name = entry_singer_name.get()
    song_year = entry_song_year.get()
    mood = mood_var.get()
    
    query = f"{singer_name} {song_year} {mood} song"
    pwk.playonyt(query)

# Create the main window
root = tk.Tk()
root.title("YouTube Video Player")

# Create and configure the entry widgets
label_video_name = tk.Label(root, text="Video Name:")
label_video_name.pack()
entry_video_name = tk.Entry(root, width=50)
entry_video_name.pack(pady=5)

label_singer_name = tk.Label(root, text="Singer Name:")
label_singer_name.pack()
entry_singer_name = tk.Entry(root, width=50)
entry_singer_name.pack(pady=5)

label_song_year = tk.Label(root, text="Year of Song:")
label_song_year.pack()
entry_song_year = tk.Entry(root, width=50)
entry_song_year.pack(pady=5)

# Create and configure the mood dropdown menu
label_mood = tk.Label(root, text="Select Mood:")
label_mood.pack()
mood_var = tk.StringVar(root)
mood_choices = ["Sad", "Romantic"]
mood_dropdown = ttk.Combobox(root, textvariable=mood_var, values=mood_choices)
mood_dropdown.pack(pady=5)
mood_dropdown.current(0)  # Set the default mood to 'Sad'

# Create and configure the button widget
play_button = tk.Button(root, text="Play Video", command=play_video)
play_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
