# Movie Recommender System
A Recommender System that suggests top 5 most similar movies to the one selected. This is a content based movie recommender system & a streamlit web application.

## Content Based Recommender Systems
* These use characteristic information and take item attributes into consideration
* These recommender systems hypothesize that if a user was interested in an item in the past, they will be interested in something similar in the future
* Items similar to the watched/selected item are selected
* Each item is represented in the form of a vector
* Recommendation are based on cosine similarity values between these vectors
* Problem arises due to making obvious recommendations based on excessive specialization. Exploration of other variety is missing.

## Download Dataset

* [Dataset link](https://www.kaggle.com/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv)

## How to run?

#### STEP 01: Clone the repo and create a conda environment

```bash
git clone https://github.com/mon28/Movie-Recommender-System.git
cd Movie-Recommender-System
conda create -n movie-rec python=3.7.10 -y
conda activate movie-rec
```

#### STEP 02: Install requirements

```bash
pip install -r requirements.txt
```

#### STEP 03: Run the Streamlit app

```bash
streamlit run app.py
```

Note: Before clicking on "Show Recommendations" for the first time, click on "Train Recommender System" for generating model