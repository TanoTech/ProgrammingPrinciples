import datetime

# class SuccessKeys(str, Enum):
#     JSON_LOADED = "json_loaded"
#     MOVIE_ADDED = "movie_added"
#     MOVIE_UPDATED = "movie_updated"
#     MOVIE_DELETED = "movie_deleted"

# class ErrorKeys(str, Enum):
#     JSON_NOT_FOUND = "json_not_found"
#     MOVIE_NOT_FOUND = "movie_not_found"
#     MOVIE_NOT_UPDATED = "movie_not_updated"
#     MOVIE_NOT_DELETED = "movie_not_deleted"
#     MOVIE_NOT_ADDED = "movie_not_added"
#     MOVIE_ALREADY_EXISTS = "movie_already_exists"
#     DIRECTOR_NOT_FOUND = "director_not_found"
#     DUPLICATED_MOVIE = "duplicated_movie"

def get_current_year():
    return datetime.datetime.now().year

CURRENT_YEAR = get_current_year()
