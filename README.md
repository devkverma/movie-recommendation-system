# Movie Recommendation System

## Overview

The Movie Recommendation System is a Python-based project that recommends movies based on user-selected titles. It leverages datasets from TMDB (The Movie Database) to analyze movie attributes such as genres, keywords, cast, production companies, and crew, using Natural Language Processing (NLP) techniques to suggest similar titles.

## Features

- **Data Integration**: Combines movie details from two datasets: `tmdb_5000_movies.csv` and `tmdb_5000_credits.csv`.
- **Data Cleaning and Extraction**: Processes the dataset to extract relevant information such as genres, keywords, cast, and crew names.
- **Tag Generation**: Creates a unique set of tags for each movie by combining multiple attributes.
- **Cosine Similarity**: Computes similarities between movie tags to identify similar films.
- **Recommendation Functionality**: Allows users to input a movie title and receive a list of recommended movies.

## Datasets

The datasets used for this project include:

1. **tmdb_5000_movies.csv**: Contains general movie information.
   - **Columns**: id, title, genres, keywords, overview, production_companies, production_countries, release_date

2. **tmdb_5000_credits.csv**: Contains information about the cast and crew of the movies.
   - **Columns**: title, cast, crew

## Installation

To run this project, ensure you have Python installed (preferably Python 3.6 or later). You will also need the following libraries:

- `numpy`
- `pandas`
- `nltk`
- `scikit-learn`

You can install these packages using pip:

```bash
pip install numpy pandas nltk scikit-learn
```

After installing, run main.py file to get `movies.pkl` and `sm.pkl`.
Then, open command prompt and run

```bash
streamlit run app.py
```


