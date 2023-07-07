from movieRecommenderSystem.config.configuration import ConfigurationManager
from movieRecommenderSystem.components.data_transformation import DataTransformation

class DataTransformationTrainingPipeline(object):
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        data_transformation_config = config.get_data_transformation_config()
        data_transformation = DataTransformation(data_transformation_config)
        data_transformation.perform_data_transformation()
