# LessBoringLife App

This Python-based application uses the TMDb API to provide information about movies. It features a graphical user interface for users to search and view movie details.This application allows users to search for movies and view similar movies based on the selected movie. It is built using the Python tkinter library for the graphical user interface and interacts with the TMDB API for fetching movie data.

## Project Structure
- `app_functions.py`: Contains `MovieFunctions` for TMDb API interactions.
- `Key.py`: Holds the TMDb API key.
- `main.py`: Main application script, establishes the GUI.
- `LICENSE`: MIT License documentation.
- `.gitignore`: Specifies files for Git to ignore.

## Installation Instructions
1. Ensure Python is installed on your system.
2. Clone the repository:
   ```
   git clone https://github.com/MeliZiba/LBL---LessBoringLife---A-movie-recommender
   ```
3. Install required packages:
   ```
   pip install -r requirements.txt
   ```
4. Insert your TMDb API key in `Key.py`.

## Usage Guidelines
- Execute `main.py` to launch the application.
- Use the GUI for searching movies. Results are based on TMDb API data.
- Enter the name of the desired movie.
- ![image](https://github.com/MeliZiba/LBL---LessBoringLife---A-movie-recommender/assets/145093756/31dbe62d-c696-44c3-b14b-52b618046c79)
- From the result page, choose the intended movie, and press show similar button to see a list of similar movies.
- ![image](https://github.com/MeliZiba/LBL---LessBoringLife---A-movie-recommender/assets/145093756/02e5500e-cf9d-4f7f-bf8f-a3c0ed313893)
- Filter the result range by entering the deisred year range.
- ![image](https://github.com/MeliZiba/LBL---LessBoringLife---A-movie-recommender/assets/145093756/d6b31a71-820d-49e9-aa47-8b83c6b293d7)
- Use Add to Playlist button to add the movie to your playlist.
- ![image](https://github.com/MeliZiba/LBL---LessBoringLife---A-movie-recommender/assets/145093756/4ccf20c6-74c9-41b3-80fc-3bd5e6ea4dd7)


## Contribution Guidelines
- Fork the repo and create a new feature or bug-fix branch.
- Follow clean code practices with comments.
- Test the application thoroughly.
- Make a pull request with a detailed description of changes.

## License
This project is under the MIT License. See `LICENSE` file for more details.

