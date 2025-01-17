import os
from typing import List, Optional, Dict, Any

from methods.movie_methods import MovieMethods


class MovieLibrary:
    
    def __init__(self, json_file: str):
        if not os.path.exists(json_file):
            raise FileNotFoundError(f"File not found: {json_file}")
        self.json_file = json_file
        self.movie_methods = MovieMethods(MovieMethods.load_json(json_file))

    def __update_json_file(self) -> None:
        self.movie_methods.save_json(self.json_file)

    def get_movies(self) -> List[Dict[str, Any]]:
        return [movie.to_dict() for movie in self.movie_methods.movies]

    def get_movie_titles(self) -> List[str]:
        return [movie.title for movie in self.movie_methods.movies]

    def count_movies(self) -> int:
        return len(self.movie_methods.movies)

    def get_movie_by_title(self, title: str) -> Optional[Dict[str, Any]]:
        movie = next((m for m in self.movie_methods.movies if m.title.lower() == title.lower()), None)
        return movie.to_dict() if movie else None

    def add_movie(self, title: str, director: str, year: int, genres: List[str]) -> Dict[str, Any]:
        movie = self.movie_methods.add_movie(title, director, year, genres)
        self.__update_json_file()
        return movie.to_dict()

    def remove_movie(self, title: str) -> Dict[str, Any]:
        movie = self.movie_methods.remove_movie(title)
        self.__update_json_file()
        return movie.to_dict()

    def update_movie(self, title: str, director: Optional[str] = None, 
                     year: Optional[int] = None, genres: Optional[List[str]] = None) -> Dict[str, Any]:
        movie = self.movie_methods.update_movie(title, director, year, genres)
        self.__update_json_file()
        return movie.to_dict()

    def get_movies_by_title_substring(self, substring: str) -> List[Dict[str, Any]]:
        return [movie.to_dict() for movie in self.movie_methods.get_movies_by_title_substring(substring)]

    def get_movies_by_year(self, year: int) -> List[Dict[str, Any]]:
        return [movie.to_dict() for movie in self.movie_methods.get_movies_by_year(year)]

    def count_movies_by_director(self, director: str) -> int:
        return self.movie_methods.count_movies_by_director(director)

    def get_movies_by_genre(self, genre: str) -> List[Dict[str, Any]]:
        return [movie.to_dict() for movie in self.movie_methods.get_movies_by_genre(genre)]

    def get_oldest_movie_title(self) -> str:
        return self.movie_methods.get_oldest_movie_title()

    def get_average_release_year(self) -> float:
        return self.movie_methods.get_average_release_year()

    def get_longest_title(self) -> str:
        return self.movie_methods.get_longest_title()

    def get_titles_between_years(self, start_year: int, end_year: int) -> List[str]:
        return self.movie_methods.get_titles_between_years(start_year, end_year)

    def get_most_common_year(self) -> int:
        return self.movie_methods.get_most_common_year()
