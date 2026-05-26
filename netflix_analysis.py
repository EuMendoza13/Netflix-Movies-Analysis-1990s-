# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Read in the Netflix CSV as a DataFrame
netflix_df = pd.read_csv("netflix_data.csv", index_col=0)
print(netflix_df)

movies = netflix_df['type'] == 'Movie'
movie_df = netflix_df[movies]

peliculas_90 = movie_df[(movie_df['release_year'] >= 1990) & (movie_df['release_year'] <= 1999)]

peliculas_action_90 = peliculas_90[peliculas_90['genre'] == 'Action']

short_movie_count = 0
for tiempo, fila in peliculas_action_90.iterrows():
	if fila['duration'] < 90:
		short_movie_count = short_movie_count + 1

print(short_movie_count)
