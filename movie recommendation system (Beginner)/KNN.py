import pandas as pd

movies = pd.read_csv("./dataset/movies.csv")
ratings = pd.read_csv("./dataset/ratings.csv")

# preparing the data for the KNN model
userMovieMatrix = ratings.pivot_table(
    index = 'user_id',
    columns = 'movieId',
    values = 'rating'
)

# knn cannot handle null so make it 0
userMovieMatrix = userMovieMatrix.fillna(0)

from sklearn.neighbors import NearestNeighbors
model = NearestNeighbors(metric='cosine', algorithm='brute')
model.fit(userMovieMatrix)

# recommendation system for a specific user
def getMovieRecommendations(user_id, userMovieMatrix, movies, n_recommendations=5):
    # change format so KNN can understand
    userVector = userMovieMatrix.loc[user_id].values.reshape(1, -1)

    distance, indices = model.kneighbors(userVector, n_neighbors=3)
    # distance = how similar, indices = which users are similar
    similarUsers = indices.flatten()

    similarUsersRatings = userMovieMatrix.iloc[similarUsers]
    meanRatings = similarUsersRatings.mean(axis=0)

    # movies the user has already rated
    userRatings = userMovieMatrix.loc[user_id]
    # filter out movies the user has already rated
    unwatchedMovies = meanRatings[userRatings == 0]

    recommendations = meanRatings[unwatchedMovies.index]
    topRecommendation = recommendations.sort_values(ascending=False).head(n_recommendations)


    # id to movie titles
    result = []
    for movieId, score in topRecommendation.items():
        title = movies[movies['movieId'] == movieId]['title'].values[0]
        result.append((title, score))
    
    return result

rec = getMovieRecommendations(1, userMovieMatrix, movies)

for title, score in rec:
    print(title, round(score, 1))