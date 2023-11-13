from tmdbv3api import TMDb, Movie
from Key import TMDB_API_Key
import tkinter as tk
import requests

class MovieFunctions:
    def initialize_movie_functions(self):
        self.tmdb = TMDb()
        self.tmdb.api_key = TMDB_API_Key
        self.movie = Movie()
        self.similar_movies_data = []

    def search_movies(self):
        try:
            movies = self.movie.search(self.movie_name_entry.get())
            movie_list = [m for m in movies if m.poster_path is not None]

            # Clear previous results
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()

            # Display search results
            for idx, m in enumerate(movie_list):
                self.display_movie(self.scrollable_frame, m, idx, self.show_similar_movies)
        except requests.exceptions.HTTPError:
            tk.messagebox.showerror("Error", "Invalid API Key or movie name. Please try again.")

    def show_similar_movies(self, movie_id):
        try:
            self.similar_movies_data = self.movie.similar(movie_id)

            # Clear previous search results and display year range filter
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()
            self.display_year_range_filter()

            self.display_similar_movies(self.similar_movies_data)
        except requests.exceptions.RequestException as e:
            tk.messagebox.showerror("Error", f"An error occurred: {e}")

    def display_year_range_filter(self):
        year_range_frame = tk.Frame(self.scrollable_frame)
        year_range_frame.grid(row=0, column=0, sticky='w')

        tk.Label(year_range_frame, text="Start Year:").pack(side='left')
        self.start_year_entry = tk.Entry(year_range_frame, width=10)
        self.start_year_entry.pack(side='left')
        
        tk.Label(year_range_frame, text="End Year:").pack(side='left')
        self.end_year_entry = tk.Entry(year_range_frame, width=10)
        self.end_year_entry.pack(side='left')

        tk.Button(year_range_frame, text="Apply Filter", command=self.apply_year_filter).pack(side='left')

    def apply_year_filter(self):
        try:
            start_year = int(self.start_year_entry.get())
            end_year = int(self.end_year_entry.get())
            if start_year > end_year:
                raise ValueError("Start year must be less than or equal to end year.")

            filtered_movies = [
                m for m in self.similar_movies_data 
                if m.release_date and start_year <= int(m.release_date[:4]) <= end_year
            ]
            self.display_similar_movies(filtered_movies)
        except ValueError as e:
            tk.messagebox.showerror("Error", "Invalid input. Please enter valid years.")

    def display_similar_movies(self, movies):
        # Clear previous movie results but keep year range filter
        for widget in self.scrollable_frame.winfo_children():
            if isinstance(widget, tk.Frame):
                continue  # Skip the year range frame
            widget.destroy()

        # Display count of similar movies
        count_label = tk.Label(self.scrollable_frame, text=f"Number of similar movies found: {len(movies)}")
        count_label.grid(row=1, column=0, sticky='w', pady=(10, 0))

        # Display similar movies
        movie_row_index = 2  # Starting index for movie rows, accounting for the year range frame and count label
        for m in movies:
            self.display_movie(self.scrollable_frame, m, movie_row_index)
            movie_row_index += 1  # Increment row index for each movie

