from tmdbv3api import TMDb, Movie
import requests
from PIL import Image, ImageTk
from io import BytesIO
import tkinter as tk
from tkinter import messagebox

def search_movies():
    tmdb = TMDb()
    tmdb.api_key = api_key_entry.get()
    movie = Movie()
    try:
        movies = movie.search(movie_name_entry.get())
        movie_list = [m for m in movies if m.poster_path is not None]
    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "Invalid API Key or movie name. Please try again.")

    selection_window = tk.Toplevel(app)
    selection_window.geometry("800x600")
    selection_window.title("Movie Selection")
    app.withdraw()  # Hide the main window

    # Close the previous window
    if hasattr(app, 'prev_window') and app.prev_window.winfo_exists():
        app.prev_window.destroy()

    app.prev_window = selection_window  # Store the current window as previous

    items_per_page = 5
    page = 1

    def display_movies(page):
        for idx, m in enumerate(movie_list[(page - 1) * items_per_page:page * items_per_page]):
            image_url = f"https://image.tmdb.org/t/p/w500{m.poster_path}"
            response = requests.get(image_url)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                image = image.resize((150, 225))
                photo = ImageTk.PhotoImage(image)
            else:
                photo = None

            tk.Label(selection_window, text=m.title).grid(row=idx, column=0)
            if photo:
                label = tk.Label(selection_window, image=photo)
                label.image = photo  # Keeping a reference to the image
                label.grid(row=idx, column=1)
            tk.Button(selection_window, text="Select", command=lambda m=m: show_similar_movies(m.id)).grid(row=idx, column=2)

        if len(movie_list) > page * items_per_page:
            tk.Button(selection_window, text="Next", command=lambda: display_movies(page + 1)).grid(row=items_per_page, column=1)

    display_movies(page)
