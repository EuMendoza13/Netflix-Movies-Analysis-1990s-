# ==========================================
# PROJECT: NETFLIX MOVIES ANALYSIS (1990s)
# ==========================================

# 1. LOADING LIBRARIES AND DATA
import pandas as pd
# Aquí va tu código para cargar el dataset, por ejemplo:
# netflix_df = pd.read_csv("netflix_data.csv")
print(netflix_df)

# 2. PART 1: MOST FREQUENT MOVIE DURATION IN THE 1990s
movies = netflix_df['type'] == 'Movie'
movie_df = netflix_df[movies]

peliculas_90 = movie_df[(movie_df['release_year'] >= 1990) & (movie_df['release_year'] <= 1999)]

duration_movie = peliculas_90['duration']

duration = duration_movie.mode()[0]

print(duration)

# 3. PART 2: SHORT ACTION MOVIES IN THE 1990s
movies = netflix_df['type'] == 'Movie'
movie_df = netflix_df[movies]

peliculas_90 = movie_df[(movie_df['release_year'] >= 1990) & (movie_df['release_year'] <= 1999)]

peliculas_action_90 = peliculas_90[peliculas_90['genre'] == 'Action']

short_movie_count = 0
for tiempo, fila in peliculas_action_90.iterrows():
	if fila['duration'] < 90:
		short_movie_count = short_movie_count + 1

print(short_movie_count)
