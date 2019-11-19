## happy path 10
* search_popularity_by_year: Which movies were more popular in [1976](release)
    - slot{"release": "1976"}
    - utter_search_popularity_by_year
    - action_listen   <!-- predicted: action_search_popularity_by_year -->
* search_overview_for_movie: give me the overview for [The Art of Self Defense](movie_title)
    - slot{"movie_title": "The Art of Self Defense"}
    - utter_search_overview_for_movie
    - action_listen   <!-- predicted: action_search_overview_for_movie -->
* search_movie_director: [Leave No Trace](movie_title) was by who?
    - slot{"movie_title": "Leave No Trace"}
    - utter_search_movie_director   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_movie_director -->
* search_movie_actors: Starring in [Spotlight](movie_title)
    - slot{"movie_title": "Spotlight"}
    - utter_search_movie_actors
    - action_listen   <!-- predicted: action_search_movie_actors -->
* search_similar_movies: movies similar to [Heat](movie_title)
    - slot{"movie_title": "Heat"}
    - utter_search_similar_movies   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_similar_movies -->


## happy path 11
* search_overview_for_movie: overview for [hp laptop](movie_title)
    - slot{"movie_title": "hp laptop"}
    - utter_search_overview_for_movie
    - action_listen   <!-- predicted: action_search_overview_for_movie -->
* search_similar_movies: suggest something like [No Country for Old Men](movie_title)
    - slot{"movie_title": "No Country for Old Men"}
    - utter_search_similar_movies   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_similar_movies -->
* search_movie_actors: which actors in [the martian](movie_title)
    - slot{"movie_title": "the martian"}
    - utter_search_movie_actors   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_movie_actors -->


## happy path 1
* greet: hello
    - utter_greet
* get_introduction: intructions
    - utter_introduction
* movie_search_by_director: Find a movie directed by [Quentin Tarantino](director)
    - slot{"director": "Quentin Tarantino"}
    - utter_movie_search_by_director
    - action_listen   <!-- predicted: action_movie_search_by_director -->
* search_movie_actors: Who starred in [It Follows](movie_title)?
    - slot{"movie_title": "It Follows"}
    - utter_search_movie_actors   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_movie_actors -->
* bye: bye   <!-- predicted: goodbye: bye -->
    - utter_bye   <!-- predicted: action_listen -->


## happy path 2
* greet: hi
    - utter_greet
* get_introduction: Tell me more about you.
    - utter_introduction
* movie_search_by_actor: where did [Philip Seymour Hoffman](actor) act in
    - slot{"actor": "Philip Seymour Hoffman"}
    - utter_movie_search_by_actor
    - action_listen   <!-- predicted: action_movie_search_by_actor -->
* release_year_search_by_movie: When was [Zombieland](movie_title) out?
    - slot{"movie_title": "Zombieland"}
    - utter_search_release_year_for_movie   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_release_year_for_movie -->
* search_rating_for_movie: how is [super dark times](movie_title) rated?
    - slot{"movie_title": "super dark times"}
    - utter_search_rating_for_movie   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_rating_for_movie -->


## happy path 3
* greet: hello
    - utter_greet
* get_introduction: how to use you?
    - utter_introduction
* movie_search_by_director: What is the director [Woody Allen](director) known for   <!-- predicted: movie_search_by_director: What is the director [Woody Allen](actor) known for -->
    - slot{"actor": "Woody Allen"}
    - utter_movie_search_by_director
    - action_listen   <!-- predicted: action_movie_search_by_director -->
* release_year_search_by_movie: give me the release for [the favourite](movie_title).
    - slot{"movie_title": "the favourite"}
    - utter_search_release_year_for_movie   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_release_year_for_movie -->
* search_overview_for_movie: give me the plot for [Match Point](movie_title)   <!-- predicted: search_overview_for_movie: give me the plot for [Match Point](movie_title:match point) -->
    - slot{"movie_title": "match point"}
    - utter_search_overview_for_movie   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_overview_for_movie -->
* search_rating_for_movie: how is [super dark times](movie_title) rated?
    - slot{"movie_title": "super dark times"}
    - utter_search_rating_for_movie
    - action_listen   <!-- predicted: action_search_rating_for_movie -->


## happy path 4
* greet: hello
    - utter_greet
* get_introduction: How do you work?
    - utter_introduction
* movie_search_by_director: What can you find me directed by [Guillermo del Toro](director?
    - utter_movie_search_by_director
    - action_listen   <!-- predicted: action_movie_search_by_director -->
* search_overview_for_movie: give me the summary for [Terminator Genesys](movie_title)
    - slot{"movie_title": "Terminator Genesys"}
    - utter_search_overview_for_movie
    - action_listen   <!-- predicted: action_search_overview_for_movie -->
* release_year_search_by_movie: out date for [black panther](movie_title)
    - slot{"movie_title": "black panther"}
    - utter_search_release_year_for_movie   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_release_year_for_movie -->
* search_rating_for_movie: give me the rating for [Spider-Man: Far from home](movie_title)
    - slot{"movie_title": "Spider-Man: Far from home"}
    - utter_search_rating_for_movie
    - action_listen   <!-- predicted: action_search_rating_for_movie -->


## happy path 5
* greet: hi
    - utter_greet
* get_introduction: instructions
    - utter_introduction
* movie_search_by_actor: In which movie [Johny Depp](actor) shot?
    - slot{"actor": "Johny Depp"}
    - utter_movie_search_by_actor
    - action_listen   <!-- predicted: action_movie_search_by_actor -->
* movie_search_by_actor: Where did [Robert De Niro](actor) star in?
    - slot{"actor": "Robert De Niro"}
    - utter_movie_search_by_actor   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: utter_movie_search_by_actor -->
* movie_search_by_actor: movies performed by [jean reno](actor)
    - slot{"actor": "jean reno"}
    - utter_movie_search_by_actor
    - action_listen   <!-- predicted: action_movie_search_by_actor -->
* search_overview_for_movie: what is the plot for [Coco](movie_title)
    - slot{"movie_title": "Coco"}
    - utter_search_overview_for_movie
    - action_listen   <!-- predicted: action_search_overview_for_movie -->
* release_year_search_by_movie: let me know when was [I am not a witch](movie_title) released?
    - slot{"movie_title": "I am not a witch"}
    - utter_search_release_year_for_movie   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_release_year_for_movie -->


## happy path 6
* greet: hello
    - utter_greet
* get_introduction: instructions
    - utter_introduction
* search_overview_for_movie: what is [The Dead Do not Die](movie_title) about?
    - slot{"movie_title": "The Dead Do not Die"}
    - utter_search_overview_for_movie
    - action_listen   <!-- predicted: action_search_overview_for_movie -->
* search_popularity_by_year: Give popular movies of [1999](release)
    - slot{"release": "1999"}
    - utter_search_popularity_by_year
    - action_listen   <!-- predicted: action_search_popularity_by_year -->
* release_year_search_by_movie: out date for [black panther](movie_title)
    - slot{"movie_title": "black panther"}
    - utter_search_release_year_for_movie   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_release_year_for_movie -->
* search_movie_director: Get me the director of [Mission Impossible Fallout](movie_title)
    - slot{"movie_title": "Mission Impossible Fallout"}
    - utter_search_movie_director   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_movie_director -->
* search_overview_for_movie: give me the summary of [Maleficient: Mistress of Evil](movie_title).
    - slot{"movie_title": "Maleficient: Mistress of Evil"}
    - utter_search_overview_for_movie
    - action_listen   <!-- predicted: action_search_overview_for_movie -->


## happy path 7
* search_popularity_by_year: give me the most popular movies of [1983](release)
    - slot{"release": "1983"}
    - utter_search_popularity_by_year
    - action_listen   <!-- predicted: action_search_popularity_by_year -->
* search_movie_director: who was [Paddington 2](movie_title) by?
    - slot{"movie_title": "Paddington 2"}
    - utter_search_movie_director   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_movie_director -->
* search_rating_for_movie: rating for [The Lure](movie_title)   <!-- predicted: search_rating_for_movie: rating for [The Lure](movie_title:the lure) -->
    - slot{"movie_title": "the lure"}
    - utter_search_rating_for_movie   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_rating_for_movie -->
* search_overview_for_movie: give me the overview for [The Art of Self Defense](movie_title)
    - slot{"movie_title": "The Art of Self Defense"}
    - utter_search_overview_for_movie
    - action_listen   <!-- predicted: action_search_overview_for_movie -->
* release_year_search_by_movie: release date for [Roma](movie_title)
    - slot{"movie_title": "Roma"}
    - utter_search_release_year_for_movie   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_release_year_for_movie -->


## happy path 8
* greet: hello
    - utter_greet
* get_introduction: instructions
    - utter_introduction
* search_popularity_by_year: what was popular in [2000](release)
    - slot{"release": "2000"}
    - utter_search_popularity_by_year
    - action_listen   <!-- predicted: action_search_popularity_by_year -->
* search_overview_for_movie: plot for [skills matter](movie_title)
    - slot{"movie_title": "skills matter"}
    - utter_search_overview_for_movie
    - action_listen   <!-- predicted: action_search_overview_for_movie -->
* search_movie_actors: Starring in [Spotlight](movie_title)
    - slot{"movie_title": "Spotlight"}
    - utter_search_movie_actors   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_movie_actors -->
* search_movie_director: [Leave No Trace](movie_title) was by who?
    - slot{"movie_title": "Leave No Trace"}
    - utter_search_movie_director   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_movie_director -->


## happy path 9
* greet: hi
    - utter_greet
* get_introduction: What do you do?
    - utter_introduction
* search_popularity_by_year: Give popular movies of [1999](release)
    - slot{"release": "1999"}
    - utter_search_popularity_by_year
    - action_listen   <!-- predicted: action_search_popularity_by_year -->
* search_overview_for_movie: what is the plot for [Coco](movie_title)
    - slot{"movie_title": "Coco"}
    - utter_search_overview_for_movie
    - action_listen   <!-- predicted: action_search_overview_for_movie -->
* search_movie_actors: actors in [Sicario](movie_title)
    - slot{"movie_title": "Sicario"}
    - utter_search_movie_actors   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_movie_actors -->
* search_movie_director: who directed [Coco](movie_title)
    - slot{"movie_title": "Coco"}
    - utter_search_movie_director   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_movie_director -->
* search_popularity_by_year: Which movies were more popular in [1976](release)
    - slot{"release": "1976"}
    - utter_search_popularity_by_year
    - action_listen   <!-- predicted: action_search_popularity_by_year -->
* search_overview_for_movie: What is the plot for [Alien](movie_title)?   <!-- predicted: search_overview_for_movie: What is the plot for [Alien](movie_title:alien)? -->
    - slot{"movie_title": "alien"}
    - utter_search_overview_for_movie
    - action_listen   <!-- predicted: action_search_overview_for_movie -->
* release_year_search_by_movie: when was [Alien](movie_title) released?   <!-- predicted: release_year_search_by_movie: when was [Alien](movie_title:alien) released? -->
    - slot{"movie_title": "alien"}
    - utter_search_release_year_for_movie   <!-- predicted: action_listen -->
    - action_listen   <!-- predicted: action_search_release_year_for_movie -->


