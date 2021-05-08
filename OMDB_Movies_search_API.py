import requests as re
import json


#name = input("Enter Movie Name : ")


class Ratings():

    def __init__(self, name):
        self.name = name
        self.baseurl = 'http://www.omdbapi.com/'

    # method to extract imdb id to get imdb ratings
    def id_extractor(self):
        params_dict = {}
        params_dict['apikey'] = 'Your_API_key'
        params_dict['s'] = self.name
        res = re.get(self.baseurl , params=params_dict)
        return res.json()['Search'][0]['imdbID']

    #Method to get Ratings from omdbapi API
    def ratings(self):
        params_dict = {}
        params_dict['apikey'] = 'e761e97' # Get API key from omdbapi.com
        params_dict['i'] = self.id_extractor()
        res = re.get(self.baseurl , params=params_dict)
        page = res.json()
        title = page['Title']
        release_date = page['Released']
        genre = page['Genre']
        imdb_rating = page['imdbRating']
        #print('Title :\t'+title+'\nReleased:\t'+release_date+'\nGenre:\t'+genre+'\nIMDB_Rating:\t'+imdb_rating)
        return [title, release_date, genre, imdb_rating]
    def __repr__(self):
        return f"Object for {self.name}"

#test = Ratings('Tenet')
#print(test.ratings())
