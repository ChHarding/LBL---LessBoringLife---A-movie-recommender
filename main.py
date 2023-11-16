import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import requests
from PIL import Image, ImageTk
from io import BytesIO
from app_functions import MovieFunctions  # Import the class with TMDB-related functions

class MovieApp(tk.Tk, MovieFunctions):
    def __init__(self):
        super().__init__()
        self.geometry("800x600")
        self.title("LessBoringLife App")
        self.initialize_movie_functions()  # Initialize TMDB-related functions
        self.create_widgets()

    def create_widgets(self):
        # Movie Search Section
        tk.Label(self, text="Enter a movie name: ", font="Calibri 10 bold").pack()
        self.movie_name_entry = tk.Entry(self, width=50)
        self.movie_name_entry.pack()
        tk.Button(self, text="Search Movies", command=self.search_movies).pack()

        # Scrolling Canvas for search results and similar movies
        self.canvas = tk.Canvas(self)
        self.scrollbar = ttk.Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion=self.canvas.bbox("all")
            )
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")

    def display_movie(self, parent, movie_data, row, command=None):
        frame = tk.Frame(parent, padx=10, pady=10)
        frame.grid(row=row, column=0, sticky='nw', pady=10)

        if movie_data.poster_path:
            image_url = f"https://image.tmdb.org/t/p/w500{movie_data.poster_path}"
            response = requests.get(image_url)
            if response.status_code == 200:
                image = Image.open(BytesIO(response.content))
                image = image.resize((100, 150))
                photo = ImageTk.PhotoImage(image)
                image_label = tk.Label(frame, image=photo)
                image_label.image = photo
                image_label.grid(row=0, column=0, rowspan=3)

        title_year = f"{movie_data.title} ({movie_data.release_date[:4]})"
        tk.Label(frame, text=title_year, font=("Arial", 12, "bold")).grid(row=0, column=1, sticky='w')

        # Display short description (overview)
        overview = tk.Label(frame, text=movie_data.overview, wraplength=400)
        overview.grid(row=1, column=1, sticky='w')

        if command:
            tk.Button(frame, text="Show Similar", command=lambda: command(movie_data.id)).grid(row=2, column=1)

# Run the application
if __name__ == "__main__":
    app = MovieApp()
    app.mainloop()
