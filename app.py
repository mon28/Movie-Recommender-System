import sys
import streamlit as st
from movieRecommenderSystem.app_exception.exception_handler import AppException
from movieRecommenderSystem.logging import logger
from movieRecommenderSystem.constants import *
from movieRecommenderSystem.config.configuration import ConfigurationManager
from movieRecommenderSystem.pipeline.inference import MovieRecommender
from main import TrainingPipeline


class App(object):
    def __init__(self, config=ConfigurationManager()):
        self.recommender = MovieRecommender()
        self.movies = self.recommender.get_movies()
    

    def train_engine(self):
        try:
            obj = TrainingPipeline()
            obj.start_training_pipeline()
            st.text("Training Completed!")
            logger.info(f"Training completed successfully!")
        except Exception as e:
            raise AppException(e, sys) from e


    def recommendation_engine(self, selected_movie):
        try:
            recommended_movies_titles, recommended_movies_posters = self.recommender.get_recommendations(selected_movie)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(recommended_movies_titles[0])
                st.image(recommended_movies_posters[0])
            
            with col2:
                st.text(recommended_movies_titles[1])
                st.image(recommended_movies_posters[1])

            with col3:
                st.text(recommended_movies_titles[2])
                st.image(recommended_movies_posters[2])

            with col4:
                st.text(recommended_movies_titles[3])
                st.image(recommended_movies_posters[3])

            with col5:
                st.text(recommended_movies_titles[4])
                st.image(recommended_movies_posters[4])
        except Exception as e:
            raise AppException(e, sys) from e

if __name__ == '__main__':
    st.header("Movie Recommendation System using Machine Learning")
    st.text("This is a content based recommendation system!")

    app = App()

    movie_list = app.movies['title'].values
    selected_movie = st.selectbox(
        'Type of select movies to get recommendations.',
        movie_list
    )

    if st.button('Train Recommender System'):
        app.train_engine()

    if st.button('Show Recommendations'):
        app.recommendation_engine(selected_movie)
        