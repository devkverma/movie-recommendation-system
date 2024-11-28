import numpy as np
import pandas as pd
import ast
from nltk.stem.snowball import SnowballStemmer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pickle

df1 = pd.read_csv("tmdb_5000_movies.csv")
df2 = pd.read_csv("tmdb_5000_credits.csv")

movies = df1.merge(df2,on='title')
movies = movies[['id','title','genres','keywords','overview','production_companies','production_countries','release_date','cast','crew']]

def extractName(object):
    name = []
    for i in ast.literal_eval(object):
        word = i['name']
        word = word.split()
        name.append("".join(word))
    return name

movies['genres'] = movies['genres'].apply(extractName)
movies['keywords'] = movies['keywords'].apply(extractName)
movies['production_companies'] = movies['production_companies'].apply(extractName)
movies['production_countries'] = movies['production_countries'].apply(extractName)

def extractName3(object):
    name = []
    counter = 0
    for i in ast.literal_eval(object):
        if counter == 3:
            break
        word = i['name']
        word = word.split()
        name.append("".join(word))
        counter += 1
    return name

movies['cast'] = movies['cast'].apply(extractName3)


def extractDir(object):
    name = []
    for i in ast.literal_eval(object):
        if i['job'] == "Director":
            word = i['name']
            word = word.split()
            name.append("".join(word))
    return name

movies['crew'] = movies['crew'].apply(extractDir)
movies.dropna(inplace=True)

movies['tags'] = movies['genres'] + movies['keywords'] + movies['production_companies'] + movies['production_countries'] + movies['cast'] + movies['crew']
movies = movies[['id','title','tags']]

stemmer = SnowballStemmer("english")

def stemwords(word):
    return stemmer.stem(word.lower())

movies['tags'] = movies['tags'].apply(lambda x:[stemwords(i) for i in x])

def joinWords(obj):
    return " ".join(obj)

movies['tags'] = movies['tags'].apply(joinWords)

cv = CountVectorizer(max_features=5000,stop_words="english")

vectors = cv.fit_transform(movies['tags']).toarray()

similarities = cosine_similarity(vectors)

with open("sm.pkl", "wb") as file:
    pickle.dump(similarities, file)


movies_dict = movies.to_dict()

with open("movies.pkl","wb") as file:
    pickle.dump(movies_dict,file)