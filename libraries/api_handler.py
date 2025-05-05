"""
API Handler library
Jon Duopu
Apr. 22nd, 2025
"""

# VARIABLES
import requests
import json
API_KEY = "b3dcb0edaec6d45f2446465c4aa6dd80"
BASE_URL = "https://api.themoviedb.org/3"

# FUNCTIONS
def search_movies_by_keyword(keyword, limit=5):
    """
    Search for movies by keyword.
    Returns a list of movies with title, overview, rating, and id.
    """
    url = f"{BASE_URL}/search/movie"
    params = {
        "api_key": API_KEY,
        "query": keyword,
        "language": "en-US"
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = json.loads(response.text)
        return [{
            "title": movie.get("title"),
            "overview": movie.get("overview"),
            "rating": movie.get("vote_average"),
            "id": movie.get("id")
        } for movie in data.get("results", [])[:limit]]
    else:
        print(f"Error: {response.status_code}")
        return []

def get_movie_details(movie_id):
    """
    Get detailed info about a movie by its ID.
    """
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        "api_key": API_KEY,
        "language": "en-US"
    }
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return json.loads(response.text)
    else:
        print(f"Error fetching movie details: {response.status_code}")
        return None


# FUNCTION CALLS
