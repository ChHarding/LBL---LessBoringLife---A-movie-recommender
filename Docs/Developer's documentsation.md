
# Project Documentation

## Introduction
This Python-based application uses the TMDb API to provide information about movies. It features a graphical user interface for users to search and view movie details.

## Step-by-Step Function Documentation

1. app_functions.py
   
   This file contains the core functionalities related to the TMDb API interactions. It includes classes and methods that handle various aspects of movie data
retrieval and processing.

    Key Functions and Their Descriptions:
- `initialize_movie_functions`: Initializes the settings and configurations for movie-related operations, and retreiveing the API key.
- `search_movies`: Implements the logic to search for movies based on user input.
- `show_similar_movies`: Returns similar movies based on user selection using TMDB API features.
- `display_year_range_filter`: Create year range filter required parts, including user inputs.
- `apply_year_filter`: Filter the results of similar movies to be in the desired year range.
- `add_to_playlist`: Will add the movie to the playlist.
- `display_similar_movies`: Display simiar movies in the related part of the app.

2. Key.py
  This file is straightforward, containing the API key necessary for accessing the TMDb API.

    Key Elements:

    TMDB_API_Key: Stores the actual API key.

3. main.py
The main.py file is the entry point of the application, where the GUI is set up and the application is started.

    Key Components and Their Descriptions:

- MovieApp Class: A class that extends the Tkinter framework to create the application window and integrate the functionalities from app_functions.py.
   - __init__ Method: Initializes the application window and sets up the necessary configurations.
   - `create_widgets`: Method to create and layout the GUI components like buttons, text entries, Playlist, etc.
   - `display_movie`: Defiens hpw information should be displayed for each movie, including, the poster, movie title and year, movie description, etc.
   - `update_playlist_display`: Will display moives added to the palylist, and display their title and year.

## Future work:
- A more roboust and engaging interface which has an optimized UX could be very useful.
- Providing movie trailers, and movie information links could be anothe milestone.

## Ongoing deployment/development
- Error handling for sting inputs and Year range filter inputs
