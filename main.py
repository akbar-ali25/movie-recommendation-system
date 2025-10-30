import pickle
import pandas as pd

# Load saved model
with open("model.pkl", "rb") as f:
    data = pickle.load(f)

similarity_matrix = data["similarity_matrix"]
user_movie_matrix = data["user_movie_matrix"]

def recommend_for_user(user_id, num_recommendations=5):
    if user_id not in user_movie_matrix.index:
        return f"User ID {user_id} not found."

    user_ratings = user_movie_matrix.loc[user_id]
    watched_movies = user_ratings[user_ratings > 0].index.tolist()
    
    scores = {}
    for movie in watched_movies:
        similar_movies = similarity_matrix[movie].sort_values(ascending=False)
        for similar_movie, score in similar_movies.items():
            if similar_movie not in watched_movies:
                scores[similar_movie] = scores.get(similar_movie, 0) + score

    # Recommend top movies
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)[:num_recommendations]
    return [movie for movie, score in sorted_scores]

if __name__ == "__main__":
    user_id = int(input("Enter User ID: "))
    recommendations = recommend_for_user(user_id)
    print("\n Recommended Movies:")
    for idx, movie in enumerate(recommendations, start=1):
        print(f"{idx}. {movie}")
