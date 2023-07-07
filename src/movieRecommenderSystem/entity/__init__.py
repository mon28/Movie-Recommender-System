from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig(object):
    root_dir: Path
    src_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class DataValidationConfig(object):
    root_dir: Path
    credits_csv_file: Path
    movies_csv_file: Path
    data_filename: Path
    cleaned_data_filename: Path

@dataclass(frozen=True)
class DataTransformationConfig(object):
    root_dir: Path
    data_path: Path
    data_file: Path
    transformed_filename: Path

@dataclass(frozen=True)
class ModelTrainerConfig(object):
    model_path: Path
    model_name: Path
    data_path: Path
    data_file: Path

@dataclass(frozen=True)
class ModelInferenceConfig(object):
    dataset_path: Path
    model_path: Path
    MOVIE_DETAILS_URL: str
    API_KEY: str
    POSTER_API_BASE_URL: str