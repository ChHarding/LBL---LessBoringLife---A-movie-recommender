
# Project Documentation

## Introduction
This Python-based application uses the TMDb API to provide information about movies. It features a graphical user interface for users to search and view movie details.

## Step-by-Step Function Documentation

1. app_functions.py
   
   This file contains the core functionalities related to the TMDb API interactions. It includes classes and methods that handle various aspects of movie data
retrieval and processing.

    Key Functions and Their Descriptions:
- initialize_movie_functions: Initializes the settings and configurations for movie-related operations.
- search_movies: Implements the logic to search for movies based on user input.

2. Key.py
  This file is straightforward, containing the API key necessary for accessing the TMDb API.

    Key Elements:

    TMDB_API_Key: Stores the actual API key.

3. main.py
The main.py file is the entry point of the application, where the GUI is set up and the application is started.

    Key Components and Their Descriptions:

- MovieApp Class: A class that likely extends the Tkinter framework to create the application window and integrate the functionalities from app_functions.py.
__init__ Method: Initializes the application window and sets up the necessary configurations.
create_widgets: Method to create and layout the GUI components like buttons, text entries, etc.

## Future work:
- A more roboust and engaging interface which has an optimized UX could be very useful.
- Providing movie trailers, and movie information links could be anothe milestone.

## Ongoing deployment/development
- Error handling for sting inputs and Year range filter inputs
