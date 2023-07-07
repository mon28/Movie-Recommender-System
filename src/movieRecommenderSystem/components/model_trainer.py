import os
import sys
import pickle
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from movieRecommenderSystem.logging import logger
from movieRecommenderSystem.app_exception.exception_handler import AppException
from movieRecommenderSystem.entity import ModelTrainerConfig


class ModelTrainer(object):
    def __init__(self, config: ModelTrainerConfig):
        try:
            self.config = config
            
        except Exception as e:
            raise AppException(e, sys) from e


    @staticmethod
    def load_numpy_array_data(file_path: str) -> np.array:
        """
        load numpy data from file
        file_path: path of file to load
        return: np.array data loaded
        """
        try:
            with open(file_path, 'rb') as file_obj:
                return np.load(file_obj)
        except Exception as e:
            raise AppException(e, sys) from e
        
    
    def train(self):
        try:
            # loading numpy array data
            file_path = os.path.join(self.config.data_path, self.config.data_file)
            vector = ModelTrainer.load_numpy_array_data(file_path)

            # training model using cosine similarity
            similarity = cosine_similarity(vector)
            logger.info(f"Similarity model vectory shape: {similarity.shape}")

            # Saving model
            model_path = os.path.join(self.config.model_path, self.config.model_name)
            pickle.dump(similarity, open(model_path, 'wb'))
            logger.info("Saving final similarity model to {model_path}")
                       
        except Exception as e:
            raise AppException(e, sys) from e

