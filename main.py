from constant import MOVIE_JSON_FILE, HELLO_WORLD
import json 
import sys
import datetime



def print_movies_json():
    with open(MOVIE_JSON_FILE, 'r') as movie_list:
        movies = json.load(movie_list)
        print(json.dumps(movies, indent=4))
    
def get_italian_time_now():
    now = datetime.datetime.now()
    print(now.strftime("%H:%M:%S"))
    
def get_venv_version():
    print(sys.version)
    
print_movies_json()

print(HELLO_WORLD.upper())

get_italian_time_now()

get_venv_version()