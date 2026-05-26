# Netflix Movies Analysis (1990s) 🎬🍿

## Project Description
This project is an Exploratory Data Analysis (EDA) performed on a Netflix dataset (`netflix_data.csv`). The main objective is to dive into the content released during the 1990s to identify patterns, specifically focusing on movie durations and the behavior of the action genre.

## Key Questions Solved
1. **What was the most frequent movie duration in the 1990s?**
   - Filtered and analyzed data starting from 1990 to find the mode of movie lengths. (Result stored in the `duration` variable).
2. **How many short action movies (less than 90 minutes) were released in that decade?**
   - Performed cross-filtering by release year, genre (Action), and duration. (Result stored in the `short_movie_count` variable).

## Technologies and Libraries Used
- **Python 3**
- **Pandas** (for data manipulation, cleaning, and filtering)
- **Matplotlib / Seaborn** (for data visualization of duration distributions)

## Key Findings 

* **Most Frequent Duration:** The analysis reveals that the most frequent movie duration during the 1990s was **94 minutes**. This indicates an industry "sweet spot" where filmmakers across genres managed to deliver complete stories while respecting the audience's attention span, rarely exceeding the 100-minute mark.
* **The Short Action Movie Scarcity:** Only **7 short action movies** (under 90 minutes) were identified from this decade. 

### Data Interpretation:
1. **Genre Evolution:** This scarcity suggests that during the 1990s, the action genre underwent a transformation. As storytelling and special effects grew more complex, filmmakers realized that an action narrative required more than 90 minutes to fully develop characters and maintain high production value.
2. **Format Optimization:** While action movies expanded their runtime, the overall data mode (94 mins) proves that for general audiences, keeping the runtime just over an hour and a half was the gold standard for engagement and theatrical distribution efficiency.
