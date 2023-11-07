import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tmdbv3api import TMDb, Movie
import requests
from PIL import Image, ImageTk
from io import BytesIO

def show_similar_movies(app, movie_id):
    year_range_window = tk.Toplevel(app)
    year_range_window.geometry("400x200")
    year_range_window.title("Year Range")
    app.withdraw()  # Hide the main window

    # Close the previous window
    if hasattr(app, 'prev_window') and app.prev_window.winfo_exists():
        app.prev_window.destroy()

    app.prev_window = year_range_window  # Store the current window as previous

    tk.Label(year_range_window, text="Enter the range of years:").pack()
    start_year_label = tk.Label(year_range_window, text="Start Year: ")
    start_year_label.pack()
    start_year_entry = tk.Entry(year_range_window, width=30)
    start_year_entry.pack()
    end_year_label = tk.Label(year_range_window, text="End Year: ")
    end_year_label.pack()
    end_year_entry = tk.Entry(year_range_window, width=30)
    end_year_entry.pack()

    search_button = tk.Button(year_range_window, text="Search", command=lambda: fetch_similar_movies(app, movie_id, start_year_entry.get(), end_year_entry.get()))
    search_button.pack()
    pass


def fetch_similar_movies(app, movie_id, start_year, end_year):
    movie = Movie()
    try:
        similar_movies = movie.similar(movie_id)
        filtered_movies = [m for m in similar_movies if start_year <= m.release_date[:4] <= end_year]

        similar_movies_window = tk.Toplevel(app)
        similar_movies_window.geometry("800x600")
        similar_movies_window.title("Similar Movies")
        app.withdraw()  # Hide the main window

        # Close the previous window
        if hasattr(app, 'prev_window') and app.prev_window.winfo_exists():
            app.prev_window.destroy()

        # Displaying the count of results at the top
        results_label = tk.Label(similar_movies_window, text=f"Displaying {len(filtered_movies)} results:")
        results_label.pack()

        canvas_similar = tk.Canvas(similar_movies_window)
        canvas_similar.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        scrollbar_similar = tk.Scrollbar(similar_movies_window, orient="vertical", command=canvas_similar.yview)
        scrollbar_similar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas_similar.configure(yscrollcommand=scrollbar_similar.set)
        canvas_similar.bind('<Configure>', lambda e: canvas_similar.configure(scrollregion=canvas_similar.bbox("all")))

        frame_similar = tk.Frame(canvas_similar)
        canvas_similar.create_window((0, 0), window=frame_similar, anchor="nw")

        display_similar_movies(frame_similar, filtered_movies)  # Call the function to display movies

    except requests.exceptions.RequestException as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def display_similar_movies(frame_similar, filtered_movies):
    for idx, m in enumerate(filtered_movies):
        movie_frame = tk.Frame(frame_similar, padx=10, pady=10)
        movie_frame.grid(row=idx, column=0, sticky='nw', pady=10)

        if m.poster_path:
            image_url = f"https://image.tmdb.org/t/p/w500{m.poster_path}"
            response = requests.get(image_url)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                image = image.resize((100, 150))  # Smaller size for layout purposes
                photo = ImageTk.PhotoImage(image)
                image_label = tk.Label(movie_frame, image=photo)
                image_label.image = photo  # Keep a reference to the image
                image_label.grid(row=0, column=0, rowspan=2)  # Poster occupies two rows

        title_year = f"{m.title} ({m.release_date[:4]})"
        title_label = tk.Label(movie_frame, text=title_year, font=("Arial", 12, "bold"))
        title_label.grid(row=0, column=1, sticky='w')

        # Text widget for the movie's overview
        overview_text = tk.Text(movie_frame, height=4, width=50, wrap='word', padx=5, pady=5)
        overview_text.insert('1.0', m.overview)
        overview_text.config(state='disabled', bg=movie_frame.cget('bg'), relief='flat', highlightthickness=0)
        overview_text.grid(row=1, column=1, sticky='w')
    

    pass
