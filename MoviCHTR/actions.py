
from rasa_core_sdk import Action
import requests
import json
import api_handler as mapi
import logging
logger = logging.getLogger(__name__)

#searching movies by actor
class ActionSearchMoviesByActor(Action):

    def name(self):
        return 'action_movie_search_by_actor'

    def run(self, dispatcher, tracker, domain):
        actor = tracker.get_slot('actor')
        
        if (actor is None or len(actor) == 0):
            dispatcher.utter_message("Sorry, I didn't get what movie are you talking about. Please try again")
            return
            
        movies = mapi.get_movies_by_crew(actor)
        if len(movies) == 0:
            dispatcher.utter_message("No movies with {} were found".format(actor))
        else: 
            dispatcher.utter_message("{} is known for the following movies:".format(actor))
            i = 1
            for movie in movies:
                dispatcher.utter_message(str(i) + ". " + movie)
                i = i+1

        return[]
        
#______________________________________________________________________        
#searching movies by director
class ActionSearchMoviesByDirector(Action):

    def name(self):
        return 'action_movie_search_by_director'

    def run(self, dispatcher, tracker, domain):
    
        director = tracker.get_slot('director')
        
        if (director is None or len(director) == 0):
            dispatcher.utter_message("Sorry, I didn't get what director are you talking about. Please try again")
            return
            
        movies = mapi.get_movies_by_crew(director)
        if len(movies) == 0:
            dispatcher.utter_message("No movies with {} were found".format(director))
        else: 
            dispatcher.utter_message("{} is known for the following movies:".format(director))
            i = 1
            for movie in movies:
                dispatcher.utter_message(str(i) + ". " + movie)
                i = i+1

        return[]
        
#______________________________________________________________________           
#searching movies by release
class ActionSearchReleaseYearForMovie(Action):

    def name(self):
        return 'action_search_release_year_for_movie'

    def run(self, dispatcher, tracker, domain):
        movie_title = tracker.get_slot('movie_title')
        
        if (movie_title is None or len(movie_title) == 0):
            dispatcher.utter_message("Sorry, I didn't get what movie are you talking about. Please try again")
            return
            
        results = mapi.get_attributes_by_movie_title(movie_title)
        if len(results) == 0:
            dispatcher.utter_message("I can't find anything with title {}".format(movie_title))
        else:
            movie = results[0]
            original_title = movie['original_title']
            release_year = movie['release_date'].split('-')[0]
            
            dispatcher.utter_message("{title} was released in {year}".format(title=original_title, year=release_year))
            
        return[]
      
#______________________________________________________________________         
#searching for movie plot/overview       
class ActionSearchOverviewForMovie(Action):

    def name(self):
        return 'action_search_overview_for_movie'
        
    def run(self, dispatcher, tracker, domain):
        movie_title = tracker.get_slot('movie_title')
        
        if (movie_title is None or len(movie_title) == 0):
            dispatcher.utter_message("Sorry, I didn't get what movie are you talking about. Please try again")
            return
        
        results = mapi.get_attributes_by_movie_title(movie_title)
        
        if len(results) == 0:
            dispatcher.utter_message("I can't find anything with title {}".format(movie_title))
        else:
            movie = results[0]
            original_title = movie['original_title']
            overview = movie['overview']
            
            dispatcher.utter_message("{title} has the following overview {overview}".format(title=original_title, overview=overview))
            
        return[]

#______________________________________________________________________   
#searching for movie ratings by movie title
class ActionSearchRatingForMovie(Action):

    def name(self):
        return 'action_search_rating_for_movie'
        
    def run(self, dispatcher, tracker, domain):
    
        movie_title = tracker.get_slot('movie_title')
        
        if (movie_title is None or len(movie_title) == 0):
            dispatcher.utter_message("Sorry, I didn't get what movie are you talking about. Please try again")
            return
        
        results = mapi.get_attributes_by_movie_title(movie_title)

        if len(results) == 0:
            dispatcher.utter_message("I can't find anything with title {}".format(movie_title))
        else:
            movie = results[0]
            original_title = movie['original_title']
            rating = movie['vote_average']
            
            dispatcher.utter_message("{title} has the following rating {rating}".format(title=original_title, rating=rating))
            
        return[]

#______________________________________________________________________   
#search popular movies by year
class ActionSearchPopularityByYear(Action):

    def name(self):
        return 'action_search_popularity_by_year'
        
    def run(self, dispatcher, tracker, domain):
        year = tracker.get_slot('release')
        
        if (year is None or len(year) == 0):
            dispatcher.utter_message("Sorry, I didn't get what date are you talking about. Please try again")
            return
            
        movies = mapi.get_popularity_by_year(year)
        
        dispatcher.utter_message("These are the most popular movies of {}".format(year))
        
        i = 1
        for movie in movies:
            dispatcher.utter_message(str(i) + ". " + movie['original_title'] + " with rating " + str(movie['vote_average']))
            i = i + 1
            
        return[]
        
#______________________________________________________________________   
#search director for specific movie
class ActionSearchMovieDirector(Action):

    def name(self):
        return 'action_search_movie_director'
        
    def run(self, dispatcher, tracker, domain):
        movie_title = tracker.get_slot('movie_title')
        
        if (movie_title is None or len(movie_title) == 0):
            dispatcher.utter_message("Sorry, I didn't get what movie are you talking about. Please try again")
            return 
        
        results = mapi.get_attributes_by_movie_title(movie_title)
        crew = mapi.get_crew_by_movie(results[0]['id'])
        
        if len(results) == 0:
            dispatcher.utter_message("I can't find anything with title {}".format(movie_title))
        else:
            for member in crew:
                if (member['job'] == 'Director'):
                    dispatcher.utter_message(results[0]['original_title'] + ' was directed by ' + member['name'])
                    
        return[]
#______________________________________________________________________   
#search actors for specific movie
class ActionSearchMovieActors(Action):

    def name(self):
        return 'action_search_movie_actors'
        
    def run(self, dispatcher, tracker, domain):
        movie_title = tracker.get_slot('movie_title')
        
        if (movie_title is None or len(movie_title) == 0):
            dispatcher.utter_message("Sorry, I didn't get what movie are you talking about. Please try again")
            return
            
        results = mapi.get_attributes_by_movie_title(movie_title)
        
        cast = mapi.get_cast_by_movie(results[0]['id'])
        
        if len(results) == 0:
            dispatcher.utter_message("I can't find anything with title {}".format(movie_title))
        else:
            dispatcher.utter_message("These actors starred in {}".format(movie_title))
            i = 1
            for member in cast:
                actor = member['name']
                character = member['character']
                dispatcher.utter_message(str(i) + ". " + actor + ' starred with character ' + character)
                i = i + 1   
                if (i > 10):
                    break
                    
        return[]
#______________________________________________________________________   
#search similar movies
class ActionSearchSimilarMovies(Action):
    
    def name(self):
        return 'action_search_similar_movies'
        
    def run(self, dispatcher, tracker, domain):
        movie_title = tracker.get_slot('movie_title')
        
        if (movie_title is None or len(movie_title) == 0):
            dispatcher.utter_message("Sorry, I didn't get what movie are you talking about. Please try again")
            return
            
        results = mapi.get_attributes_by_movie_title(movie_title)
        
        similar = mapi.get_similar_movies(results[0]['id'])
        
        if len(results) == 0:
            dispatcher.utter_message("I can't find anything similar to title {}".format(movie_title))
        else:
            dispatcher.utter_message("These are similar to {}".format(movie_title))
            i = 1
            for member in similar:
                suggestion = member['original_title']
                release = member['release_date']
                dispatcher.utter_message(str(i) + ". " + suggestion + ' released in  ' + release)
                i = i + 1   
                if (i > 10):
                    break
                    
        return[]
        
                                   
