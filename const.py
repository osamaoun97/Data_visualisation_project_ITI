import re
import numpy as np
from wrangle import load_data
import base64


DATA_PATH = "./data/netflix_titles.csv"

def image_source(img):
    image_filename = f'assets/{img}'
    encoded_image = base64.b64encode(open(image_filename, 'rb').read())
    src='data:image/png;base64,{}'.format(encoded_image.decode())
    return src

MOV_COLOR = "#cccccc"
SHOW_COLOR = "#831010"

df = load_data(DATA_PATH)

RATINGS_AGE = {
    "TV-PG": "Older Kids",
    "TV-MA": "Adults",
    "TV-Y7-FV": "Older Kids",
    "TV-Y7": "Older Kids",
    "TV-14": "Teens",
    "R": "Adults",
    "TV-Y": "Kids",
    "NR": "Adults",
    "PG-13": "Teens",
    "TV-G": "Kids",
    "PG": "Older Kids",
    "G": "Kids",
    "UR": "Adults",
    "NC-17": "Adults",
}

MONTHS = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

df_copy = load_data(DATA_PATH).copy(deep=True)
df_copy["country"] = df_copy["country"].replace("Missing", np.nan)
df_copy = df_copy.dropna(subset=["country"])
countries = set(list(re.split("\s?,\s?", ", ".join(df_copy["country"].to_list()))))
countries.remove("")
COUNTRIES = sorted(list(countries))

countries_shows = set(
    list(
        re.split(
            "\s?,\s?",
            ", ".join(df_copy["country"][df_copy["type"] == "TV Show"].to_list()),
        )
    )
)
countries_shows.remove("")
COUNTRIES_SHOWS = sorted(list(countries_shows))

countries_movies = set(
    list(
        re.split(
            "\s?,\s?",
            ", ".join(df_copy["country"][df_copy["type"] == "Movie"].to_list()),
        )
    )
)
countries_movies.remove("")
COUNTRIES_MOVIES = sorted(list(countries_movies))

df_copy["listed_in"] = df_copy["listed_in"].replace("Missing", np.nan)
df_copy = df_copy.dropna(subset=["listed_in"])
set1 = df_copy["listed_in"][df_copy["type"] == "TV Show"]
set2 = df_copy["listed_in"][df_copy["type"] == "Movie"]
GENRES_SHOWS = sorted(list(set(list(re.split("\s?,\s?", ", ".join(set1.to_list()))))))
GENRES_MOVIES = sorted(set(list(list(re.split("\s?,\s?", ", ".join(set2.to_list()))))))


NUM_MOVIES = df_copy["type"].value_counts()["Movie"]
NUM_SHOWS = df_copy["type"].value_counts()["TV Show"]