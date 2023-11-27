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

            # Display count of all movies found
            count_label = tk.Label(self.scrollable_frame, text=f"Number of movies found: {len(movie_list)}")
            count_label.grid(row=0, column=0, sticky='w', pady=(10, 0))

            # Display search results
            for idx, m in enumerate(movie_list, start=1):  # Note: start index changed to 1
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

            # Debugging output
            print(f"Number of similar movies found: {len(self.similar_movies_data)}")

            # Display count of all similar movies found at row=1
            count_label = tk.Label(self.scrollable_frame, text=f"Number of similar movies found: {len(self.similar_movies_data)}")
            count_label.grid(row=1, column=0, sticky='w', pady=(10, 0))

            # Start displaying movies from row=2
            movie_row_index = 2  
            for m in self.similar_movies_data:
                self.display_movie(self.scrollable_frame, m, movie_row_index)
                movie_row_index += 1

            # Refresh the window (optional, try if label is still not visible)
            self.scrollable_frame.update_idletasks()

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

            # Clear everything including the year range frame
            for widget in self.scrollable_frame.winfo_children():
                widget.destroy()

            # Re-add the year range frame
            self.display_year_range_filter()

            # Display the count of filtered movies at row=1
            count_label = tk.Label(self.scrollable_frame, text=f"Number of filtered movies: {len(filtered_movies)}")
            count_label.grid(row=1, column=0, sticky='w', pady=(10, 0))

            # Start displaying movies from row=2
            movie_row_index = 3
            for m in filtered_movies:
                self.display_movie(self.scrollable_frame, m, movie_row_index)
                movie_row_index += 1

            self.display_similar_movies(filtered_movies)

        except ValueError as e:
            tk.messagebox.showerror("Error", "Invalid input. Please enter valid years.")

    def add_to_playlist(self, movie):
        if not hasattr(self, 'playlist'):
            self.playlist = []

        movie_info = {'id': movie.id, 'title': movie.title, 'year': movie.release_date[:4]}
        if movie_info not in self.playlist:
            self.playlist.append(movie_info)
            self.update_playlist_display()  # Refresh the playlist display
            
    def display_similar_movies(self, movies):
        # Start displaying movies from the second row, as the first row is the year range frame
        movie_row_index = 2  
        for m in movies:
            self.display_movie(self.scrollable_frame, m, movie_row_index)
            movie_row_index += 1
