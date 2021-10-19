import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult', "imdb_code, title, duration, director year, rating, imdb_score,keywords, genres")

def find_movies(search_text):
    if not search_text or not search_text.strip():
        raise ValueError("Search text is required")


    url = f"https://movieservice.talkpython.fm/api/search/{search_text}"

    resp = requests.get(url)
    resp.raise_for_status()

    movie_data = resp.json()
    movies_list = movie_data.get("hits")


# added list comprehension with **kwargs
    movies = [
        MovieResult(**md)
        for md in movies_list
    ]

    movies.sort(key=lambda m: -m.year)

    return movies







