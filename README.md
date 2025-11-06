# Movie Recommendation System

## Overview

This is a beginner-friendly Movie Recommendation System built using Collaborative Filtering (User-Based or Item-Based).  
It uses the MovieLens "ml-latest-small" dataset to recommend movies to users based on their viewing and rating history.

---

## Features Implemented

* Personalized movie recommendations using Collaborative Filtering  
* User-based similarity to find users with similar tastes  
* Simple command-line interface (no Flask or web framework)  
* Works directly with the MovieLens dataset  

---

## Project Structure

```
movie-recommender/
├── main.py               # Entry point to run the recommendation system
├── recommendation.py     # Core recommendation logic
├── data/
│   ├── movies.csv
│   └── ratings.csv
├── README.md             # Project documentation
└── requirements.txt      # Python dependencies
```

---

## How It Works

1. The system loads user ratings from the dataset (`ratings.csv`).
2. It computes the similarity between users using cosine similarity.
3. For a given user, it finds other users with similar preferences.
4. Based on those similar users, it recommends movies the current user has not seen yet.

---

## Example Flow

```
Enter User ID: 10

Recommended Movies:
1. The Godfather (1972)
2. Fight Club (1999)
3. The Dark Knight (2008)
4. The Matrix (1999)
```

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <your-repo-link>
cd movie-recommender
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate      # For Linux/Mac
venv\Scripts\activate         # For Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Add Dataset
Place the downloaded `movies.csv` and `ratings.csv` inside the **data/** folder.

### 5. Run the Program
```bash
python main.py
```

---

## User IDs Information

* User IDs are fetched directly from the dataset (`ratings.csv`).
* To see all available user IDs, you can add this snippet:

```python
import pandas as pd
ratings = pd.read_csv('data/ratings.csv')
print("Available User IDs:", ratings['userId'].unique())
```

---

## Technologies Used

* Python  
* Pandas  
* NumPy  
* Scikit-learn  
* MovieLens Dataset  

---

## Future Enhancements

* Add Item-Based Filtering  
* Integrate Movie Posters using TMDB API  
* Implement Matrix Factorization (SVD/ALS)  
* Deploy as a REST API or Streamlit App  

---

## Contribution

Feel free to fork this repository, experiment with algorithms, and submit pull requests.  
All contributions are welcome.

---

## License

This project is open-source under the MIT License.

---

