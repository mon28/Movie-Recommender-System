import os
import sys
import ast
import pandas as pd
import pickle
from nltk.stem import PorterStemmer
from movieRecommenderSystem.logging import logger
from movieRecommenderSystem.app_exception.exception_handler import AppException
from movieRecommenderSystem.entity import DataValidationConfig


class DataValidation(object):
    def __init__(self, config: DataValidationConfig):
        try:
            self.config = config
            
        except Exception as e:
            raise AppException(e, sys) from e
        
    
    @staticmethod
    def convert_str_to_list(text):
        L = []
        for i in ast.literal_eval(text):
            L.append(i['name'])
        return L
    

    @staticmethod
    def convert_cast(text):
        L = []
        counter = 0
        for i in ast.literal_eval(text):
            if counter < 3:
                L.append(i['name'])
            counter += 1
        return L
    

    @staticmethod
    def fetch_director(text):
        L = []
        for i in ast.literal_eval(text):
            if i['job'] == 'Director':
                L.append(i['name'])
                break
        return L
    

    @staticmethod
    def remove_space(L):
        L1 = []
        for i in L:
            L1.append(i.replace(" ", ""))
        return L1
    

    @staticmethod
    def stems(text):
        T = []
        ps = PorterStemmer()
        for i in text.split():
            T.append(ps.stem(i))
        return " ".join(T)
    

    def preprocess_data(self):
        try:
            movies = pd.read_csv(self.config.movies_csv_file)
            credits = pd.read_csv(self.config.credits_csv_file)

            logger.info(f"Shape of movies data file: {movies.shape}")
            logger.info(f"Shape of credits data file: {credits.shape}")

            # Merging credits with movies based on title
            movies = movies.merge(credits, on="title")

            # Keeping important columns for recommendation
            movies = movies[['movie_id', 'title', 'overview', 'genres', 'keywords', 'cast', 'crew']]
            # Dropping missing values
            movies.dropna(inplace=True)

            # Converting genres from string to list
            movies['genres'] = movies['genres'].apply(DataValidation.convert_str_to_list)
            # Converting keywords column to list
            movies['keywords'] = movies['keywords'].apply(DataValidation.convert_str_to_list)
            # Keeping to 3 cast
            movies['cast'] = movies['cast'].apply(DataValidation.convert_cast)
            # Keeping Director job title
            movies['crew'] = movies['crew'].apply(DataValidation.fetch_director)
            # Converting overview to list
            movies['overview'] = movies['overview'].apply(lambda x: x.split())

            # Remove spaces from above columns
            movies['keywords'] = movies['keywords'].apply(DataValidation.remove_space)
            movies['cast'] = movies['cast'].apply(DataValidation.remove_space)
            movies['crew'] = movies['crew'].apply(DataValidation.remove_space)
            movies['overview'] = movies['overview'].apply(DataValidation.remove_space)

            # Concatinating all column into a single - tags
            movies['tags'] = movies['overview'] + movies['genres'] + movies['keywords'] + movies['cast'] + movies['crew']

            # Dropping extra columns
            movies_df = movies[['movie_id', 'title', 'tags']]
            # Converting list to str
            movies_df.loc[:, 'tags'] = movies_df['tags'].apply(lambda x: " ".join(x))
            # Converting to lowercase
            movies_df.loc[:, 'tags'] = movies_df['tags'].apply(lambda x: x.lower())
            # Stemming text
            movies_df.loc[:, 'tags'] = movies_df['tags'].apply(DataValidation.stems)

            logger.info(f"Shape of final data: {movies_df.shape}")

            # Saving cleaned data for transformation
            movies_df.to_csv(os.path.join(self.config.root_dir, self.config.cleaned_data_filename), index=False)
            logger.info(f"Saved cleaned data to {self.config.root_dir}")

            # Saving processed data for web app
            movies_serialized = movies[['movie_id', 'title']]
            pickle.dump(movies_serialized, open(os.path.join(self.config.root_dir, self.config.data_filename), 'wb'))
            logger.info(f"Saved serialized object to {self.config.root_dir}")

        except Exception as e:
            raise AppException(e, sys) from e
        
        


            



