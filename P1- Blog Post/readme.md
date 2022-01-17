# Udacity Data Science Nanodegree (Project Blog Post)
### Jean Carlos da Cruz

This repo contains the notebook and data source used in the Projet Blog Post from my Udacity's Data Science Nanodegree activity.
<br>Blog Post: https://medium.com/@cruzjeanc/not-all-hollywood-movies-are-profitable-d0fad4ee54b9</br>

## Motivations:
I decided to use this dataset because I'm passionate about movies and wanted to discover some insights about revenue and profit in movies. The dataset is pretty awesome, having information about 10,000 movies collected from The Movie Database (TMDb), including user ratings and revenue
The goal here is to answer the following questions: 

<ul>
<li><a href="#top10_revenue">Which movies are in the top#10 movies by revenue?</a></li>
<li><a href="#biggest_number_movies">Wich production company has the biggest number of movies reliesed?</a></li>
<li><a href="#companies_spent">Wich production company had spent the most?</a></li>
<li><a href="#higher_revenue">Wich production company had the higher revenue?</a></li>
<li><a href="#profit_movie">Is there any movie that were not profitable? Is yes, how many?</a></li>
<li><a href="#profit_trend">How the profit changed over years? Movies got more profitable over years?</a></li>

## Libraries:
- numpy
- pandas
- csv
- datetime
- matplotlib

## Files in Repository:

- readme.md: Relevant notes about the repository and analysis made in this project;
- tmdb-movies.csv: Dataset used in the notebook;
- IMDB_Movies_Investigation.ipynb: Jupyter notebook containing all analysis made.


## Conclusions

- The top#10 movies by revenue are: Avatar, Star Wars, The Exorcist, Jaws, Star Wars: The Force Awakens, E.T., The Net, One Hundred and One Dalmatians and The Avengers;
- The production company with the biggest number of movies reliesed is **Universal Pictures**, altough it is not the company with the higher revenue;
- The company that had spent the most is **Warner Bros.** with an estimation of $7.9B;

- The company that had the higher revenue is **Paramount Pictures** with an estimation of $26.4B;
- Unlikely, we may think. There were 1051 movies that made no profit.
- Profit increased over years. Mostly of the increase came after the year 2000.
- Runtime decreased over years. Indicating that movies got shorter as the years went by, probabily indicating that people after 1990 with other distractions becoming more popular (like TV and internet) don't have that much time to spend on movies.

### Limitations
- I've lost some of the data in the data cleaning steps where the dataset did not have the revenue and budget of the movies, which has affected our analysis by reducing the number of movie samples; 
- Data provided it is not up-to-date (revenue and budget are calculated to 2010);
- Budget and revenue column do not have currency unit;
- I was not able to calculate the exact impact of each production company on budget and revenue, since the data is concatenated within all companies in one row, the best fisible option was to assume that all production company had the same weight in budget and revenue.
