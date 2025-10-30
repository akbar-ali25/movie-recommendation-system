import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pickle

# Load data
movies = pd.read_csv("data/movies.csv")
ratings = pd.read_csv("data/ratings.csv")

# Merge
data = pd.merge(ratings, movies, on='movieId')

# Create pivot table (users as rows, movies as columns)
user_movie_matrix = data.pivot_table(index='userId', columns='title', values='rating')
user_movie_matrix.fillna(0, inplace=True)

# Compute cosine similarity between movies
movie_similarity = cosine_similarity(user_movie_matrix.T)
movie_similarity_df = pd.DataFrame(movie_similarity, 
                                   index=user_movie_matrix.columns, 
                                   columns=user_movie_matrix.columns)

# Save model and matrix
with open("model.pkl", "wb") as f:
    pickle.dump({
        "similarity_matrix": movie_similarity_df,
        "user_movie_matrix": user_movie_matrix
    }, f)

print("✅ Model training completed and saved as model.pkl")
