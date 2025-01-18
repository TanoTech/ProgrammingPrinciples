import os
from typing import List, Dict, Any, Optional
from exceptions.exception_handler import MovieNotFoundError
from methods.movie_methods import MovieMethods

class MovieLibrary:
    def __init__(self, json_file: str):
        """Initialize MovieLibrary with path to JSON file."""
        if not os.path.exists(json_file):
            raise FileNotFoundError(f"File not found: {json_file}")
        
        self.json_file = json_file
        self.movie_methods = MovieMethods()
        self.movies = self.movie_methods.load_movies_from_json(json_file)

    def __update_json_file(self) -> None:
        """update the json file, it will be used in all crud operations """
        self.movies = self.movie_methods.get_movies_dicts()
        self.movie_methods.save_movies_to_json(self.json_file, self.movies)

    def get_movies(self) -> List[Dict[str, Any]]:
        """get all movies"""
        return self.movies

    # @handle_operation(SuccessKeys.MOVIE_ADDED, ErrorKeys.MOVIE_NOT_ADDED)
    def add_movie(self, title: str, director: str, year: int, genres: List[str]) -> Dict[str, Any]:
        """add a new movie """
        movie_dict = self.movie_methods.add_movie_entry(title, director, year, genres)
        self.__update_json_file()
        return movie_dict

    # @handle_operation(SuccessKeys.MOVIE_DELETED, ErrorKeys.MOVIE_NOT_FOUND)
    def remove_movie(self, title: str) -> Dict[str, Any]:
        """remove a movie """
        movie = self.movie_methods.find_movie_by_title(title)
        if not movie:
            raise MovieNotFoundError()
        
        movie_dict = movie.to_dict()
        self.movie_methods.movies.remove(movie)
        self.__update_json_file()
        return movie_dict

    # @handle_operation(SuccessKeys.MOVIE_UPDATED, ErrorKeys.MOVIE_NOT_FOUND)
    def update_movie(self, title: str, director: Optional[str] = None, 
                     year: Optional[int] = None, genres: Optional[List[str]] = None) -> Dict[str, Any]:
        """update movie details by title"""
        movie = self.movie_methods.find_movie_by_title(title)
        if not movie:
            raise MovieNotFoundError()
        
        if director is not None:
            movie.director = director
        if year is not None:
            movie.year = year
        if genres is not None:
            movie.genres = genres
            
        self.__update_json_file()
        return movie.to_dict()

    def get_movie_titles(self) -> List[str]:
        """gives a list of all movie titles."""
        return [movie["title"] for movie in self.movies]

    def count_movies(self) -> int:
        """gives the total movies number."""
        return len(self.movies)

    def get_movie_by_title(self, title: str) -> Optional[Dict[str, Any]]:
        """return a movie from its title."""
        movie = self.movie_methods.find_movie_by_title(title)
        return movie.to_dict() if movie else None

    def get_movies_by_title_substring(self, substring: str) -> List[Dict[str, Any]]:
        """return movies with the specific substring."""
        matching_movies = [
            movie for movie in self.movie_methods.movies 
            if substring in movie.title
        ]
        return [movie.to_dict() for movie in matching_movies]

    def get_movies_by_year(self, year: int) -> List[Dict[str, Any]]:
        """gives all movies from that year"""
        matching_movies = [
            movie for movie in self.movie_methods.movies 
            if movie.year == year
        ]
        return [movie.to_dict() for movie in matching_movies]

    def count_movies_by_director(self, director: str) -> int:
        """give the total movies from a director"""
        return len([
            movie for movie in self.movie_methods.movies 
            if MovieMethods.compare_strings_case_insensitive(movie.director, director)
        ])

    def get_movies_by_genre(self, genre: str) -> List[Dict[str, Any]]:
        """all movies of a specific genre."""
        matching_movies = [
            movie for movie in self.movie_methods.movies 
            if any(MovieMethods.compare_strings_case_insensitive(g, genre) 
                  for g in movie.genres)
        ]
        return [movie.to_dict() for movie in matching_movies]

    def get_oldest_movie_title(self) -> str:
        """giveds the title of the oldest movie."""
        oldest_movie = min(self.movie_methods.movies, key=lambda x: x.year)
        return oldest_movie.title

    def get_average_release_year(self) -> float:
        """average of realease year of the movie in the library"""
        return sum(movie.year for movie in self.movie_methods.movies) / len(self.movie_methods.movies)

    def get_longest_title(self) -> str:
        """return the longest movie title"""
        return max(self.movie_methods.movies, key=lambda x: len(x.title)).title

    def get_titles_between_years(self, start_year: int, end_year: int) -> List[str]:
        """return titles of movies between a periodo of years"""
        return [
            movie.title for movie in self.movie_methods.movies 
            if start_year <= movie.year <= end_year
        ]

    def get_most_common_year(self) -> int:
        """return the most frequent release year."""
        years = [movie.year for movie in self.movie_methods.movies]
        return max(set(years), key=years.count)
