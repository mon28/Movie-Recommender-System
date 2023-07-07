from movieRecommenderSystem.config.configuration import ConfigurationManager
from movieRecommenderSystem.components.data_ingestion import DataIngestion

class DataIngestionTrainingPipeline(object):
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()