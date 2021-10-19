import requests
import collections

MovieResult = collections.namedtuple(
    'MovieResult', "imdb_code, title, duration, director year, rating, imdb_score,keywords, genres")


# search = "park"
# search = "the shawshank redemption"

search = input("What movie you are searching for?")
url = f"https://movieservice.talkpython.fm/api/search/{search}"

resp = requests.get(url)
resp.raise_for_status()

movie_data = resp.json()
movies_list= movie_data.get("hits")

# movies = []
# for md in movies_list:
#     m = MovieResult(
#         imdb_code=md.get("imdb_code"),
#         title=md.get("title"),
#         duration=md.get("duration"),
#         director=md.get("director"),
#         year=md.get("year", 0),
#         rating=md.get("rating", 0),
#         imdb_score=md.get("imdb_score", 0.0),
#         keywords=md.get("keywords"),
#         genres=md.get("genres"))
#     movies.append(m)

# movies = []
# for md in movies_list:
#     m = MovieResult(**md)
#     movies.append()
# **kwargs work only when the keyword arguments exactly match with the keys in the tuple [IMPORTANT]


movies = [
    MovieResult(**md)
    for md in movies_list    # added list comprehension with **kwargs
]

print(f"Found {len(movies)} movies for search {search}")
for m in movies:
    print(f"{m.year} -- {m.title}")








