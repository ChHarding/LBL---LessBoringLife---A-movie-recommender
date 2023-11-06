import tkinter as tk
from tkinter import messagebox
from movies import search_movies

# Initializing the Tkinter app
app = tk.Tk()
app.geometry("400x200")
app.title("LessBoringLife App")

# Step 2: Input for the user to enter a movie name
movie_name_label = tk.Label(app, text="Enter a movie name: ", font="Calibri 10 bold")
movie_name_label.pack()
movie_name_entry = tk.Entry(app, width=50)
movie_name_entry.pack()

# Run the main loop for the application
search_button = tk.Button(app, text="Search Movies", command=lambda: search_movies(app, movie_name_entry))
search_button.pack()
app.mainloop()
