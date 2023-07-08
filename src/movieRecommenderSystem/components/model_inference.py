import requests
import sys
import pickle
from movieRecommenderSystem.logging import logger
from movieRecommenderSystem.app_exception.exception_handler import AppException
from movieRecommenderSystem.entity import ModelInferenceConfig


class ModelInference(object):
    def __init__(self, config: ModelInferenceConfig):
        try:
            self.config = config
            self.movies = pickle.load(open(config.dataset_path, 'rb'))
            self.similarity = pickle.load(open(config.model_path, 'rb'))
            
        except Exception as e:
            raise AppException(e, sys) from e

        
    def get_recommendations(self, movie_name):
        try:
            index = self.movies[self.movies['title'] == movie_name].index[0]
            distances = sorted(list(enumerate(self.similarity[index])), reverse=True, key=lambda x: x[1])
            recommended_movies_titles = []
            recommended_movies_posters = []
            if len(distances) > 0:
                for d in distances[1:6]:
                    movie_id = self.movies.iloc[d[0]].movie_id
                    movie_name = self.movies.iloc[d[0]].title
                    recommended_movies_posters.append(self.fetch_poster(movie_id))
                    recommended_movies_titles.append(movie_name)
            return recommended_movies_titles, recommended_movies_posters
        except Exception as e:
            raise AppException(e, sys) from e
        
    
    def fetch_poster(self, movie_id):
        try:
            url = self.config.MOVIE_DETAILS_URL.format(movie_id, self.config.API_KEY)
            movie_details = requests.get(url)
            movie_details_json = movie_details.json()
            poster_path = movie_details_json["poster_path"] if movie_details_json["poster_path"] else ""
            return self.config.POSTER_API_BASE_URL + poster_path
        except Exception as e:
            raise AppException(e, sys) from e
        
    
    def get_movies(self):
        return self.movies