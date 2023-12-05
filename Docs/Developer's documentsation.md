
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

## Application walkthrough
- Execute `main.py` to launch the application.
- Use the GUI for searching movies. Results are based on TMDb API data.
-<img src="https://github.com/MeliZiba/LBL---LessBoringLife---A-movie-recommender/assets/145093756/c084425b-a48e-4c50-894d-81bc718dab38" width="800" height="600">
- Enter the name of the desired movie.
- <img src="https://github.com/MeliZiba/LBL---LessBoringLife---A-movie-recommender/assets/145093756/31dbe62d-c696-44c3-b14b-52b618046c79"  width="350" height="70">
- From the result page, choose the intended movie, and press show similar button to see a list of similar movies.
- <img src="https://github.com/MeliZiba/LBL---LessBoringLife---A-movie-recommender/assets/145093756/02e5500e-cf9d-4f7f-bf8f-a3c0ed313893" width="120" height="70">

- Filter the result range by entering the deisred year range.
- <img src="https://github.com/MeliZiba/LBL---LessBoringLife---A-movie-recommender/assets/145093756/d6b31a71-820d-49e9-aa47-8b83c6b293d7" width="350" height="70">
- Use Add to Playlist button to add the movie to your playlist.
- <img src="https://github.com/MeliZiba/LBL---LessBoringLife---A-movie-recommender/assets/145093756/4ccf20c6-74c9-41b3-80fc-3bd5e6ea4dd7" width="90" height="40">

## Future work:
- A more roboust and engaging interface which has an optimized UX could be very useful.
- Providing movie trailers, and movie information links could be anothe milestone.

## Ongoing deployment/development
- Error handling for sting inputs and Year range filter inputs
