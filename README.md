# Multipurpose-web-app-using-flask

## Live Project on Intertnet link
- http://smit271.pythonanywhere.com/

## Used APIs to create this project
- I used following APIs to create different functionalities.
- 1> OpenWeatherAPI for getting weather details from https://api.openweathermap.org/data/2.5/weather
- 2> NASA_API to get pictures of mars clicked by different rovers
- 3> OMDB_API to get IMDB Ratings and movie details
- 4> Advice to print Advice on home screen after refreshing page
- 5> Datamuse_API to get synonyms of searched word.
- 6> Flicker_API to get photos url by tag name 

## Used Technologies :
- Python Flask : For Backend
- HTML
- CSS
- Bootstrap : to give site some actions and logic 
- JavaScript : (to Show Time on home page)
- Diffrent API

## Directory/file  : Work

- static : hold 'css' and 'javascripts' files
- templates : hold 'HTML' and 'image' files
- Current_Weather_API.py : python file to get weather details
- OMDB_Movies_search_API.py : getting movies details 
- advice.py : getting random advice
- datamuse_api.py : getting synonyms of word
- flickr_api.py : Flicker_API to get photos url
- app.py : flask file to start server
- form.py : python file generating forms using WTF
- requirement.txt : External library name & versions
- subscribers.db/ txt : Database file


## Requirements

- First run following command to download external library
- python3 -m pip install -r requirement.txt
- After completed go to Run part.


## How to start Flask-Server

- Go to project directory then run following command
- python3 app.py
- go to link given in terminal during starting kernel
