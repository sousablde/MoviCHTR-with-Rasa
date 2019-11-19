
## fallback
  - utter_greet

## greeting path 1
* greet
  - utter_greet

## get movie by actor
* movie_search_by_actor
  - utter_movie_search_by_actor
  - action_movie_search_by_actor

## get movie by director
* movie_search_by_director
  - utter_movie_search_by_director
  - action_movie_search_by_director

## get release year for given movie
* release_year_search_by_movie
  - utter_search_release_year_for_movie
  - action_search_release_year_for_movie

## get overview for movie
* search_overview_for_movie
  - utter_search_overview_for_movie
  - action_search_overview_for_movie
  
## get rating for movie
* search_rating_for_movie
  - utter_search_rating_for_movie
  - action_search_rating_for_movie

## get popular movies by year
* search_popularity_by_year
  - utter_search_popularity_by_year
  - action_search_popularity_by_year

## get movie director 
* search_movie_director
  - utter_search_movie_director
  - action_search_movie_director
  
## get movie actors
* search_movie_actors
  - utter_search_movie_actors
  - action_search_movie_actors
  
## get similar movies
* search_similar_movies
  - utter_search_similar_movies
  - action_search_similar_movies

## get introduction
* get_introduction
  - utter_introduction

## bye path 1
* bye
  - utter_bye
  
## happy path 1
* greet
  - utter_greet
* get_introduction
  - utter_introduction
* movie_search_by_director{"director":"Oliver Stone"}
  - slot{"director":"Oliver Stone"}
  - utter_movie_search_by_director
  - action_movie_search_by_director
* search_movie_actors{"movie_title":"Fight Club"}
  - slot{"movie_title":"Fight Club"}
  - utter_search_movie_actors
  - action_search_movie_actors  
* bye
  - utter_bye
    
## happy path 2
* greet
  - utter_greet
* get_introduction
  - utter_introduction
* movie_search_by_actor{"actor":"Brad Pitt"}
  - slot{"actor":"Brad Pitt"}
  - utter_movie_search_by_actor
  - action_movie_search_by_actor
* release_year_search_by_movie{"movie_title":"Fight Club"}
  - slot{"movie_title":"Fight Club"}
  - utter_search_release_year_for_movie
  - action_search_release_year_for_movie
* search_rating_for_movie{"movie_title":"Fight Club"}
  - slot{"movie_title":"Fight Club"}
  - utter_search_rating_for_movie
  - action_search_rating_for_movie

## happy path 3
* greet
  - utter_greet
* get_introduction
  - utter_introduction
* movie_search_by_director{"director":"Ridley Scott"}
  - slot{"director":"Ridley Scott"}
  - utter_movie_search_by_director
  - action_movie_search_by_director
* release_year_search_by_movie{"movie_title":"Alien"}
  - slot{"movie_title":"Alien"}
  - utter_search_release_year_for_movie
  - action_search_release_year_for_movie
* search_overview_for_movie{"movie_title":"Alien"}
  - slot{"movie_title":"Alien"}
  - utter_search_overview_for_movie
  - action_search_overview_for_movie
* search_rating_for_movie{"movie_title":"Alien"}
  - slot{"movie_title":"Alien"}
  - utter_search_rating_for_movie
  - action_search_rating_for_movie

## happy path 4
* greet
  - utter_greet
* get_introduction
  - utter_introduction
* movie_search_by_director{"director":"Stanley Kubrick"}
  - slot{"director":"Stanley Kubrick"}
  - utter_movie_search_by_director
  - action_movie_search_by_director
* search_overview_for_movie{"movie_title":"The Shining"}
  - slot{"movie_title":"The Shining"}
  - utter_search_overview_for_movie
  - action_search_overview_for_movie
* release_year_search_by_movie
  - utter_search_release_year_for_movie
  - action_search_release_year_for_movie
* search_rating_for_movie{"movie_title":"The Shining"}
  - slot{"movie_title":"The Shining"}
  - utter_search_rating_for_movie
  - action_search_rating_for_movie

## happy path 5
* greet
  - utter_greet
* get_introduction
  - utter_introduction
* movie_search_by_actor{"actor":"Jennifer Lawrence"}
  - slot{"actor":"Jennifer Lawrence"}
  - utter_movie_search_by_actor
  - action_movie_search_by_actor
* movie_search_by_actor{"actor":"Sting"}
  - slot{"actor":"Sting"}
  - utter_movie_search_by_actor
  - action_movie_search_by_actor
* movie_search_by_actor{"actor":"Brad Pitt"}
  - slot{"actor":"Brad Pitt"}
  - utter_movie_search_by_actor
  - action_movie_search_by_actor
* search_overview_for_movie{"movie_title":"Se7en"}
  - slot{"movie_title":"Se7en"}
  - utter_search_overview_for_movie
  - action_search_overview_for_movie
* release_year_search_by_movie{"movie_title":"Se7en"}
  - slot{"movie_title":"Se7en"}
  - utter_search_release_year_for_movie
  - action_search_release_year_for_movie
  
## happy path 6
* greet
    - utter_greet
* get_introduction
    - utter_introduction
* search_overview_for_movie{"movie_title":"alien"}
    - slot{"movie_title":"alien"}
    - utter_search_overview_for_movie
    - action_search_overview_for_movie
* search_popularity_by_year{"release":"2019"}
    - slot{"release":"2019"}
    - utter_search_popularity_by_year
    - action_search_popularity_by_year
* release_year_search_by_movie{"movie_title":"Joker"}
    - slot{"movie_title":"Joker"}
    - utter_search_release_year_for_movie
    - action_search_release_year_for_movie
* search_movie_director{"movie_title":"Joker"}
    - slot{"movie_title":"Joker"}
    - utter_search_movie_director
    - action_search_movie_director
* search_overview_for_movie
    - slot{"movie_title":"Joker"}
    - utter_search_overview_for_movie
    - action_search_overview_for_movie
    
## happy path 7
* search_popularity_by_year{"release":"2019"}
    - slot{"release":"2019"}
    - utter_search_popularity_by_year
    - action_search_popularity_by_year
* search_movie_director{"movie_title":"Logan"}
    - slot{"movie_title":"Logan"}
    - utter_search_movie_director
    - action_search_movie_director
* search_rating_for_movie{"movie_title":"Logan"}
  - slot{"movie_title":"Logan"}
  - utter_search_rating_for_movie
  - action_search_rating_for_movie
* search_overview_for_movie{"movie_title":"Logan"}
    - slot{"movie_title":"Logan"}
    - utter_search_overview_for_movie
    - action_search_overview_for_movie
* release_year_search_by_movie{"movie_title":"Logan"}
    - slot{"movie_title":"Logan"}
    - utter_search_release_year_for_movie
    - action_search_release_year_for_movie
    
## happy path 8
* greet
    - utter_greet
* get_introduction
    - utter_introduction
* search_popularity_by_year{"release":"1994"}
    - slot{"release":"1994"}
    - utter_search_popularity_by_year
    - action_search_popularity_by_year
* search_overview_for_movie{"movie_title":"Pulp Fiction"}
    - slot{"movie_title":"Pulp Fiction"}
    - utter_search_overview_for_movie
    - action_search_overview_for_movie
* search_movie_actors{"movie_title":"Pulp Fiction"}
    - slot{"movie_title":"Pulp Fiction"}
    - utter_search_movie_actors
    - action_search_movie_actors
* search_movie_director{"movie_title":"Pulp Fiction"}
    - slot{"movie_title":"Pulp Fiction"}
    - utter_search_movie_director
    - action_search_movie_director

## happy path 9
* greet
    - utter_greet
* get_introduction
    - utter_introduction
* search_popularity_by_year{"release":"1994"}
    - slot{"release":"1994"}
    - utter_search_popularity_by_year
    - action_search_popularity_by_year
* search_overview_for_movie{"movie_title":"Pulp Fiction"}
    - slot{"movie_title":"Pulp Fiction"}
    - utter_search_overview_for_movie
    - action_search_overview_for_movie
* search_movie_actors{"movie_title":"Pulp Fiction"}
    - slot{"movie_title":"Pulp Fiction"}
    - utter_search_movie_actors
    - action_search_movie_actors
* search_movie_director{"movie_title":"Pulp Fiction"}
    - slot{"movie_title":"Pulp Fiction"}
    - utter_search_movie_director{"movie_title":"Pulp Fiction"}
    - action_search_movie_director
* search_popularity_by_year{"release":"2018"}
    - slot{"release":"2018"}
    - utter_search_popularity_by_year
    - action_search_popularity_by_year
* search_overview_for_movie{"movie_title":"Black Panther"}
    - slot{"movie_title":"Black Panther"}
    - utter_search_overview_for_movie
    - action_search_overview_for_movie
* release_year_search_by_movie{"movie_title":"Black Panther"}
    - slot{"movie_title":"Black Panther"}
    - utter_search_release_year_for_movie
    - action_search_release_year_for_movie
    
## happy path 10
* search_popularity_by_year{"release":"2007"}
    - slot{"release":"2007"}
    - utter_search_popularity_by_year
    - action_search_popularity_by_year
* search_overview_for_movie{"movie_title":"Coco"}
    - slot{"movie_title":"Coco"}
    - utter_search_overview_for_movie
    - action_search_overview_for_movie
* search_movie_director{"movie_title":"Coco"}
    - slot{"movie_title":"Coco"}
    - utter_search_movie_director{"movie_title":"Coco"}
    - action_search_movie_director
* search_movie_actors{"movie_title":"Coco"}
    - slot{"movie_title":"Coco"}
    - utter_search_movie_actors
    - action_search_movie_actors
* search_similar_movies{"movie_title":"Coco"}
    - slot{"movie_title":"Coco"}
    - utter_search_similar_movies
    - action_search_similar_movies 
    
## happy path 11
* search_overview_for_movie{"movie_title":"Coco"}
    - slot{"movie_title":"Coco"}
    - utter_search_overview_for_movie
    - action_search_overview_for_movie
* search_similar_movies{"movie_title":"Coco"}
    - slot{"movie_title":"Coco"}
    - utter_search_similar_movies
    - action_search_similar_movies
* search_movie_actors{"movie_title":"Coco"}
    - slot{"movie_title":"Coco"}
    - utter_search_movie_actors
    - action_search_movie_actors

