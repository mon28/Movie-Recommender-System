from movieRecommenderSystem.config.configuration import ConfigurationManager
from movieRecommenderSystem.components.data_validation import DataValidation

class DataValidationTrainingPipeline(object):
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(data_validation_config)
        data_validation.preprocess_data()
