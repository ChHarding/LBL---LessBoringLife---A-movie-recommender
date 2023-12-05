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
4. Insert your TMDb API key in `Key.py`. To have a TMDB API, you need to go to https://www.themoviedb.org/signup, and create an account. and from https://www.themoviedb.org/settings/api get your API key. Enter your API key in `Key.py`.

## Usage Guidelines
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


## Contribution Guidelines
- Fork the repo and create a new feature or bug-fix branch.
- Follow clean code practices with comments.
- Test the application thoroughly.
- Make a pull request with a detailed description of changes.

## License
This project is under the MIT License. See `LICENSE` file for more details.

