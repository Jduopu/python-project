"""
The main handler for the project
Jon Duopu
Apr. 22nd, 2025
"""

# VARIABLES
API_KEY = "b3dcb0edaec6d45f2446465c4aa6dd80"
BASE_URL = "https://api.themoviedb.org/3"

# IMPORTS
from libraries import api_handler

# FUNCTIONS
def get_movie_genre(genre):
    movies = api_handler.search_movies_by_keyword(genre)
    if not movies:
        print("No movies found.")
        return
    for i, movie in enumerate(movies, start=1):
        print(f"\n{i}. {movie['title']} ({movie['rating']}/10)")
        print(f"   {movie['overview']}")
    return movies

def get_movie_details(id):
    details = api_handler.get_movie_details(id)
    if details:
        print(f"\nTitle: {details['title']}")
        print(f"Tagline: {details.get('tagline', 'No tagline')}")
        print(f"Release Date: {details['release_date']}")
        print(f"Runtime: {details['runtime']} minutes")
        print(f"Overview: {details['overview']}")
    else:
        print("Could not retrieve details.")

def main():
    genre = input("Enter a movie genre or mood: ")
    movies = get_movie_genre(genre)

    if movies:
        try:
            index = int(input("\nEnter the number of a movie to get more details: ")) - 1
            if 0 <= index < len(movies):
                get_movie_details(movies[index]['id'])
            else:
                print("Invalid selection.")
        except ValueError:
            print("Please enter a valid number.")

# FUNCTION CALLS
main()
