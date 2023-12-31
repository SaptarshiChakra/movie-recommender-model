import streamlit as st
import pickle
import pandas as pd
import requests

def fetch_poster(movie_id):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=1bd3573d3cb4837d94e69173bef89009&language=en-US'.format(movie_id)
    data = requests.get(url)
    data = data.json()
    return "https://image.tmdb.org/t/p/w500/"+data['poster_path']


def recommend_names(movie):
    movie_index = movies[movies.title == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommended_movies = []
    for i in movie_list[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


def recommend_posters(movie):
    movie_index = movies[movies.title == movie].index[0]
    distances = similarity[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])

    recommended_movies_posters=[]
    for i in movie_list[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies_posters.append(fetch_poster(movie_id))
    return recommended_movies_posters


movie_dict = pickle.load(open('dictionary' ,'rb'))
movies = pd.DataFrame(movie_dict)

similarity = pickle.load(open('similarity.pkl','rb'))

st.title("Movie Recommender System")

selected_movie_name = st.selectbox(
    'Which type to movie do you want to get recommended',
    movies['title'].values)

if st.button('Show Recommendation'):
    recommended_movie_names = recommend_names(selected_movie_name)
    recommended_movie_posters = recommend_posters(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])