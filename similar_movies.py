import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from tmdbv3api import TMDb, Movie
import requests
from PIL import Image, ImageTk
from io import BytesIO
from Key import TMDB_API_Key

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

        items_per_page = 5
        page = 1
        canvas_similar = tk.Canvas(similar_movies_window)
        canvas_similar.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        scrollbar_similar = ttk.Scrollbar(similar_movies_window, orient=tk.VERTICAL, command=canvas_similar.yview)
        scrollbar_similar.pack(side=tk.RIGHT, fill=tk.Y)

        canvas_similar.configure(yscrollcommand=scrollbar_similar.set)
        canvas_similar.bind('<Configure>', lambda e: canvas_similar.configure(scrollregion=canvas_similar.bbox("all")))

        frame_similar = tk.Frame(canvas_similar)
        canvas_similar.create_window((0, 0), window=frame_similar, anchor="nw")


        def display_similar_movies(page, frame_similar):
            for idx, m in enumerate(filtered_movies[(page - 1) * items_per_page:page * items_per_page]):
                if m.poster_path:
                    image_url = f"https://image.tmdb.org/t/p/w500{m.poster_path}"
                    response = requests.get(image_url)
                if response.status_code == 200:
                    image = Image.open(BytesIO(response.content))
                    image = image.resize((150, 225))
                    photo = ImageTk.PhotoImage(image)
                    label = tk.Label(frame_similar, text=f"{m.title} ({m.release_date[:4]}) - {m.overview[:100]}")
                    label.image = photo  # Keeping a reference to the image
                    label.grid(row=idx, column=0)
                    image_label = tk.Label(frame_similar, image=photo)
                    image_label.image = photo  # Keeping a reference to the image
                    image_label.grid(row=idx, column=1)
                else:
                    tk.Label(frame_similar, text=f"{m.title} ({m.release_date[:4]}) - {m.overview[:100]}").grid(row=idx, column=0)

            if len(filtered_movies) > page * items_per_page:
                tk.Button(frame_similar, text="Next", command=lambda: display_similar_movies(page + 1, frame_similar)).grid(row=items_per_page, column=1)

        display_similar_movies(page, frame_similar)

    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "Something went wrong. Please try again.")


    pass
