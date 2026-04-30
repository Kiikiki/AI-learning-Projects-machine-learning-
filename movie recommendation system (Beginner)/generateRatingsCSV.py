import pandas as pd
import numpy as np
import os 

movies = pd.read_csv("./dataset/movies.csv")

# making fake users ratings
num_users = 10

userPreference = {
    1: ["Horror", "Documentary"],
    2: ["Action", "Comedy"],
    3: ["Romance", "Sci-Fi"],
    4: ["Comedy", "Romance"],
    5: ["Action", "Sci-Fi"],
    6: ["Horror", "Action"],
    7: ["Documentary", "Drama"],
    8: ["Comedy", "Action"],
    9: ["Romance", "Drama"],
    10: ["Sci-Fi", "Action"]
}

ratingList = []

for user_id in range(1, num_users+1):
    # randomly select 100 - 400 movies for each user
    watched = movies.sample(n=np.random.randint(100, 200))

    for _, row in watched.iterrows():
        genres = str(row["genres"])

        preferredGenres = any(genre in genres for genre in userPreference[user_id])

        if preferredGenres:
            # if the movie has a preferred genre, give it a higher rating
            rating = round(np.random.uniform(4.0, 5.0), 1)
        else:
            # if not, give it a lower rating
            rating = round(np.random.uniform(1.0, 2.5), 1)

        ratingList.append({
            "user_id": user_id,
            "movieId": row["movieId"],
            # ratings between 1 and 5 and rounded to 1 decimal place
            "rating": rating  
        })

ratings = pd.DataFrame(ratingList)          # Convert the list of ratings to a DataFrame aka ratings.csv
ratings.to_csv("./dataset/ratings.csv", index=False)  # Save the ratings DataFrame to a CSV file