import streamlit as st
import pandas as pd
import requests
import pickle
from concurrent.futures import ThreadPoolExecutor

API_KEY = "2b828244e61525fc7ea34cd70e412b44"

# Cache data loading to avoid reloading on each rerun
@st.cache_resource
def load_data():
    with open("movies.tkl", "rb") as file:
        movies_dict = pickle.load(file)

    movies = pd.DataFrame(movies_dict)

    with open("sm.tkl", "rb") as file:
        similarities = pickle.load(file)

    return movies, similarities

movies, similarities = load_data()

# Cache API call to reduce repetitive requests for the same movie ID
@st.cache_data(show_spinner=False)
def get_poster_url(movieId):
    url = f'https://api.themoviedb.org/3/movie/{movieId}?api_key={API_KEY}'
    response = requests.get(url)
    data = response.json()
    poster_path = data.get('poster_path')
    image_base_url = 'https://image.tmdb.org/t/p/w500'
    return f'{image_base_url}{poster_path}' if poster_path else None

def recommend(movieName):
    movieIndex = movies.index[movies['title'] == movieName][0]
    recommended_movies = []

    for i, sim in sorted(enumerate(similarities[movieIndex]), reverse=True, key=lambda x: x[1])[1:6]:
        recommended_movies.append((movies['title'][i], movies['id'][i]))

    return recommended_movies

# Function to fetch all poster URLs in parallel using ThreadPoolExecutor
def fetch_posters(movie_ids):
    with ThreadPoolExecutor() as executor:
        poster_urls = list(executor.map(get_poster_url, movie_ids))
    return poster_urls

st.title("Movies Recommendation System")

# Dropdown for movie selection
option = st.selectbox(
    "Search a movie",
    movies['title']
)

_, mid_column, _ = st.columns(3)

if mid_column.button("Recommend"):
    # Get recommended movies
    recommended_movies = recommend(option)
    movie_ids = [id for name, id in recommended_movies]

    # Fetch poster URLs in parallel
    poster_urls = fetch_posters(movie_ids)

    # Display recommended movies and posters
    col1, col2, col3, col4, col5 = st.columns(5)
    columns = {0: col1, 1: col2, 2: col3, 3: col4, 4: col5}

    col_0, col_1, col_2, col_3, col_4 = st.columns(5)
    image_columns = {0:col_0,1:col_1,2:col_2,3:col_3,4:col_4}

    for i, (name, poster_url) in enumerate(zip([name for name, id in recommended_movies], poster_urls)):
        columns[i].write(name)
        if poster_url:
            image_columns[i].image(poster_url)
        else:
            image_columns[i].write("No poster available")
