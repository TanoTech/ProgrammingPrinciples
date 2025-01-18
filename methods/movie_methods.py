from typing import List, Dict, Any, Optional
import json
from entities.movie import Movie
from constant.constants import CURRENT_YEAR

class MovieMethods:
    def __init__(self):
        """Use Movie class to initialize constructor"""
        self.movies: List[Movie] = []

    @staticmethod
    def clean_string(s: str) -> str:
        return s.strip().lower()

    @staticmethod
    def compare_strings_case_insensitive(s1: str, s2: str) -> bool:
        return MovieMethods.clean_string(s1) == MovieMethods.clean_string(s2)

    def load_movies_from_json(self, file_path: str) -> List[Dict[str, Any]]:
        """load from the json file e gives dictionary"""
        with open(file_path, 'r') as f:
            movies_data = json.load(f)
            self.movies = [Movie.from_dict(movie) for movie in movies_data]
            return movies_data

    def save_movies_to_json(self, file_path: str, movies_data: List[Dict[str, Any]]) -> None:
        """save movies to json"""
        with open(file_path, 'w') as f:
            json.dump(movies_data, f, indent=4)

    def add_movie_entry(self, title: str, director: str, year: int, genres: List[str]) -> Dict[str, Any]:
        """ input validation """
        if not title or not title.strip():
            raise ValueError("Title cannot be empty")
        if not director or not director.strip():
            raise ValueError("Director cannot be empty")
        if not genres:
            raise ValueError("Genres list cannot be empty")
        if not isinstance(genres, list) or not all(isinstance(g, str) for g in genres):
            raise ValueError("Genres must be a list of strings")
        if not isinstance(year, int):
            raise ValueError("Year must be an integer")
            
        """check if the movie exists"""
        existing_movie = self.find_movie_by_title(title)
        if existing_movie:
            raise ValueError("Movie already exists in the library")
            
        """check if the year is correct"""
        if year < 1895 or year > CURRENT_YEAR:
            raise ValueError(f"Year must be between 1895 and {CURRENT_YEAR}")
        
        """strings cleaning"""
        title = title.strip()
        director = director.strip()
        genres = [g.strip() for g in genres if g.strip()]
        
        movie = Movie(title=title, director=director, year=year, genres=genres)
        self.movies.append(movie)
        return movie.to_dict()

    def find_movie_by_title(self, title: str) -> Optional[Movie]:
        """find by title case insensitive"""
        return next(
            (movie for movie in self.movies 
             if self.compare_strings_case_insensitive(movie.title, title)),
            None
        )

    def get_movies_dicts(self) -> List[Dict[str, Any]]:
        """makes all movies from json to dictionary"""
        return [movie.to_dict() for movie in self.movies]