import os
import sys
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from movieRecommenderSystem.logging import logger
from movieRecommenderSystem.app_exception.exception_handler import AppException
from movieRecommenderSystem.entity import DataTransformationConfig


class DataTransformation(object):
    def __init__(self, config: DataTransformationConfig):
        try:
            self.config = config
            
        except Exception as e:
            raise AppException(e, sys) from e
        

    
    @staticmethod
    def save_numpy_array_data(file_path: str, array: np.array):
        """
        Save numpy array data to file
        file_path: str location of file to save
        array: np.array data to save
        """
        try:
            with open(file_path, 'wb') as file_obj:
                np.save(file_obj, array)
        except Exception as e:
            raise AppException(e, sys) from e
        

    
    def perform_data_transformation(self):
        try:
            data_df = pd.read_csv(os.path.join(self.config.data_path, self.config.data_file))
            cv = CountVectorizer(max_features=5000, stop_words='english')
            vector = cv.fit_transform(data_df['tags']).toarray()
            logger.info(f"Shape of the final vector: {vector.shape}")

            # Saving vector as numpy array for training
            DataTransformation.save_numpy_array_data(file_path=os.path.join(self.config.root_dir, self.config.transformed_filename), array=vector)
            logger.info(f"Saving final vector as numpy array to {self.config.root_dir}")
        except Exception as e:
            raise AppException(e, sys) from e
        
