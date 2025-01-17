from typing import List, Optional
import json
from exceptions.exception_handler import MovieNotFoundError,SuccessKeys, ErrorKeys, handle_operation
from constant.constants import CURRENT_YEAR
from entities.movie import Movie

class MovieMethods:

    def __init__(self, movies: Optional[List[Movie]] = None):
        self.movies = movies or []

    @staticmethod
    def load_json(file_path: str) -> List[Movie]:
        with open(file_path, 'r') as f:
            movies_data = json.load(f)
            return [Movie.from_dict(movie) for movie in movies_data]

    def save_json(self, file_path: str) -> None:
        movies_data = [movie.to_dict() for movie in self.movies]
        with open(file_path, 'w') as f:
            json.dump(movies_data, f, indent=4)

    def add_movie(self, title: str, director: str, year: int, genres: List[str]) -> Movie:
        if not title or not director or not year or not genres:
            raise ValueError("All fields are required")
        if year < 1895 or year > CURRENT_YEAR:
            raise ValueError("Year must be between 1895 and ${CURRENT_YEAR}")
        movie = Movie(title=title, director=director, year=year, genres=genres)
        self.movies.append(movie)
        return movie

    def remove_movie(self, title: str) -> Movie:
        movie = next((m for m in self.movies if m.title.lower() == title.lower()), None)
        if not movie:
            raise MovieNotFoundError()
        self.movies.remove(movie)
        return movie

    def update_movie(self, title: str, 
                     director: Optional[str] = None, 
                     year: Optional[int] = None, 
                     genres: Optional[List[str]] = None) -> Movie:
        movie = next((m for m in self.movies if m.title.lower() == title.lower()), None)
        if not movie:
            raise MovieNotFoundError()
        
        if director:
            movie.director = director
        if year:
            movie.year = year
        if genres:
            movie.genres = genres
        return movie
    
    def get_movies_by_title_substring(self, substring: str) -> List[Movie]:
        return [movie for movie in self.movies if substring in movie.title]

    def get_movies_by_year(self, year: int) -> List[Movie]:
        return [movie for movie in self.movies if movie.year == year]

    def count_movies_by_director(self, director: str) -> int:
        return len([movie for movie in self.movies if movie.director.lower() == director.lower()])

    def get_movies_by_genre(self, genre: str) -> List[Movie]:
        return [movie for movie in self.movies if genre.lower() in [g.lower() for g in movie.genres]]

    def get_oldest_movie_title(self) -> str:
        return min(self.movies, key=lambda x: x.year).title

    def get_average_release_year(self) -> float:
        return sum(movie.year for movie in self.movies) / len(self.movies)

    def get_longest_title(self) -> str:
        return max(self.movies, key=lambda x: len(x.title)).title

    def get_titles_between_years(self, start_year: int, end_year: int) -> List[str]:
        return [movie.title for movie in self.movies if start_year <= movie.year <= end_year]

    def get_most_common_year(self) -> int:
        years = [movie.year for movie in self.movies]
        return max(set(years), key=years.count)
