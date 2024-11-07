import pickle
import streamlit as st
import pandas as pd
import requests


def fetch_poster(movie_id):
    response = requests.get(
        'https://api.themoviedb.org/3/movie/{}?api_key=8fa892b2250d2fcf4bfb165f00e65a49'.format(movie_id))
    data = response.json()
    print(data)
    return "http://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_movies_posters = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        # fetch posters from API
        recommended_movies_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_movies_posters


# Load movie data and similarity data
movies_dict = pickle.load(open("movie_dict.pkl", "rb"))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))

st.header('Movie Recommender System')

# Add a text input with a placeholder for user guidance
selected_movie_name = st.selectbox(
    "Type in an option or pick from the dropdown menu:",
    options=[""] + movies["title"].values.tolist(),  # Add an empty string as the first option
    index=0  # Default selection is the empty option, effectively removing "Avatar"
)

if st.button('Show Recommendation'):
    if selected_movie_name:  # Check if a movie has been selected
        recommended_movie_names, recommended_movie_posters = recommend(selected_movie_name)

        col1, col2, col3, col4, col5 = st.columns(5)  # Create 5 columns for layout
        for col, poster, name in zip([col1, col2, col3, col4, col5], recommended_movie_posters,
                                     recommended_movie_names):
            with col:
                st.image(poster, use_column_width=True)  # Display the poster
                st.write(name)  # Display the full movie name under the poster

    else:
        st.warning("Please select a movie from the dropdown menu.")  # Prompt to select a movie
