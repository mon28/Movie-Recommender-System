from movieRecommenderSystem.config.configuration import ConfigurationManager
from movieRecommenderSystem.components.model_inference import ModelInference

class MovieRecommender(object):
    def __init__(self):
        config = ConfigurationManager()
        model_inference_config = config.get_model_inference_config()
        self.model_inference = ModelInference(model_inference_config)

    def get_recommendations(self, movie_name): 
        return self.model_inference.get_recommendations(movie_name)
    
    def get_movies(self):
        return self.model_inference.get_movies()