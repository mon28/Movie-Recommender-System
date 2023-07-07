import os
import sys

from movieRecommenderSystem.constants import *
from movieRecommenderSystem.utils.common import read_yaml, create_directories
from movieRecommenderSystem.entity import (DataIngestionConfig,
                                           DataValidationConfig,
                                           DataTransformationConfig,
                                           ModelTrainerConfig,
                                           ModelInferenceConfig)

class ConfigurationManager(object):
    def __init__(self, 
                 config_filepath=CONFIG_FILE_PATH):
        self.config = read_yaml(config_filepath)

        create_directories([self.config.artifacts_root])

    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            src_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )
        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            credits_csv_file=config.credits_csv_file,
            movies_csv_file=config.movies_csv_file,
            data_filename=config.data_filename,
            cleaned_data_filename=config.cleaned_data_filename
        )
        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir=config.root_dir,
            data_path=config.data_path,
            data_file=config.data_file,
            transformed_filename=config.transformed_filename
        )
        return data_transformation_config


    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_training
        create_directories([config.model_path])

        model_trainer_config = ModelTrainerConfig(
            model_path=config.model_path,
            model_name=config.model_name,
            data_path=config.data_path,
            data_file=config.data_file
        )
        return model_trainer_config


    def get_model_inference_config(self) -> ModelInferenceConfig:
        config = self.config.model_inference

        model_inference_config = ModelInferenceConfig(
            dataset_path=config.dataset_path,
            model_path=config.model_path,
            MOVIE_DETAILS_URL=config.MOVIE_DETAILS_URL,
            API_KEY=config.API_KEY,
            POSTER_API_BASE_URL=config.POSTER_API_BASE_URL
        )
        return model_inference_config