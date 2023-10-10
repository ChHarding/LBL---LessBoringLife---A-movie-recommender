from fuzzywuzzy import fuzz
from tmdbv3api import TMDb
from tmdbv3api import Movie
from PIL import Image, ImageTk
import requests

# Initialize the TMDb API
tmdb = TMDb()
tmdb_movie = Movie()

# Function to perform a fuzzy search for movies
def search_movies(user_input):
    search_results = []

    # Search for movies using fuzzy matching
    for movie in tmdb_movie.search(user_input):
        similarity = fuzz.partial_ratio(user_input.lower(), movie['title'].lower())
        if similarity > 70:  # Adjust the similarity threshold as needed
            search_results.append(movie)

    return search_results

# Function to display similar movies based on user selection
def show_similar_movies(selected_movie):
    similar_movies = tmdb_movie.similar(selected_movie['id'])

    similar_results = []

    # Display up to 5 similar movies
    for movie in similar_movies:
        year = movie.get('release_date', '').split('-')[0]
        title = movie.get('title', '')
        description = movie.get('overview', '')
        poster_path = movie.get('poster_path', '')
        poster_url = f"https://image.tmdb.org/t/p/w500/{poster_path}" if poster_path else ''

        # Load and display the poster image
        poster_image = Image.open(requests.get(poster_url, stream=True).raw)
        poster_image = poster_image.resize((120, 180), Image.ANTIALIAS)

        similar_results.append({
            'title': title,
            'year': year,
            'description': description,
            'poster_image': poster_image
        })

    return similar_results
