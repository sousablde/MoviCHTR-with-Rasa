
import requests
import json

#Global Variables
API_KEY = '6b49e5c8d23f64805bba6f86bb2fe4cd'
BASE_URL = 'https://api.themoviedb.org/3/'

#defining subject entity search queries

#popular movies
def get_popularity_by_year(year):
    #adding API endpoint (discover)
    url = BASE_URL + 'discover/movie'
    
    #parameter specification
    params = {'api_key': API_KEY, 'sort_by' : 'popularity.desc', 'include_adult' : 'false', 'primary_release_year' : year}
    
    #perform request
    response = requests.get(url, params = params).text
    
    response_json = json.loads(response)
    
    #get results array
    results = response_json['results']
    
    return results
    
#get known movies by crew person (example: actor/ director)
def get_movies_by_crew(query):
    url = BASE_URL + 'search/multi'
    
    params = {'api_key': API_KEY, 'query' : query, 'include_adult' : 'false'}  
    
    response = requests.get(url, params = params).text
    
    response_json = json.loads(response)
    
    results = response_json['results']
    
    movies = parseMoviesWith(results, query)
    
    return movies
  

#get credits by movie title (example: who directed/acted in movie?)
def get_crew_by_movie(query):
    url = BASE_URL + 'movie/{}/credits'.format(query)
    
    params = {'api_key': API_KEY}  
    
    response = requests.get(url, params = params).text
    
    response_json = json.loads(response)
    
    crew = response_json['crew']
    
    return crew   
    
#get cast by movie title (example: who directed/acted in movie?)
def get_cast_by_movie(query):
    url = BASE_URL + 'movie/{}/credits'.format(query)
    
    params = {'api_key': API_KEY}  
    
    response = requests.get(url, params = params).text
    
    response_json = json.loads(response)
    
    cast = response_json['cast']
    
    return cast  
    

#get movie attributes by movie_title (example: rating/release_year)
def get_attributes_by_movie_title(query):
    url = BASE_URL + 'search/movie'
    
    params = {'api_key': API_KEY, 'query' : query, 'include_adult' : 'false'}
    
    response = requests.get(url, params = params).text
    
    response_json = json.loads(response)
    
    if (response_json.get('results') == None):
        print("Error requesting attributes for query")
        return None
    
    results = response_json['results']
    
    return results


#finds known for movies for given person
def parseMoviesWith(json_data, person):
    movies = []

    for results in json_data:
        if results['media_type'] == 'person':
            known_for = results['known_for']
            for movie in known_for:
                title = movie['original_title']
                movies.append(title)

    return movies
    
#finds movies similar to inputted title
def get_similar_movies(query):
    url = BASE_URL + 'movie/{}/similar'.format(query)
    
    params = {'api_key': API_KEY}  
    
    response = requests.get(url, params = params).text
    
    response_json = json.loads(response)
    
    if (response_json.get('results') == None):
        print("Error requesting attributes for query")
        return None
        
    results = response_json['results']
    
    return results
    
