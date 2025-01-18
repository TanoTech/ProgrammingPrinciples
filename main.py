import os
import json
from entities.movie_library import MovieLibrary
from constant.config import MOVIE_JSON_FILE
from exceptions.exception_handler import MovieNotFoundError

def main():
    # Create data folder and json fil if they don't exist
    os.makedirs("data", exist_ok=True)

    if not os.path.exists(MOVIE_JSON_FILE):
        with open(MOVIE_JSON_FILE, 'w') as f:
            json.dump([], f)

    # Test success case: 
    try:
        library = MovieLibrary(MOVIE_JSON_FILE)

        print("\n--- Testing Success Cases ---\n")

        # Add movies
        print("Adding movies:")
        library.add_movie("Inception    ", "Christopher Nolan", 2010, ["Action", "Sci-Fi", "Thriller"])
        library.add_movie("The Shawshank Redemption      ", "Frank Darabont", 1994, ["Drama"])
        library.add_movie("The Dark Knight       ", "Christopher Nolan", 2008, ["Action", "Crime", "Drama"])

        # Get movies
        print("\nGetting all movies:")
        movies = library.get_movies()
        for movie in movies:
            print(movie)

        # Update movie
        print("\nUpdating a movie:")
        library.update_movie("Inception", director="Chris Nolan", year=2011)

        # Remove movie
        print("\nRemoving a movie:")
        library.remove_movie("The Shawshank Redemption")

        # Others methods
        print("\nMovie titles:", library.get_movie_titles())
        print("Number of movies:", library.count_movies())
        print("Movie by title:", library.get_movie_by_title("Inception"))
        print("Movies by title substring:", library.get_movies_by_title_substring("Dark"))
        print("Movies by year:", library.get_movies_by_year(2008))
        print("Count movies by director:", library.count_movies_by_director("Christopher Nolan"))
        print("Movies by genre:", library.get_movies_by_genre("Action"))
        print("Oldest movie title:", library.get_oldest_movie_title())
        print("Average release year:", library.get_average_release_year())
        print("Longest title:", library.get_longest_title())
        print("Titles between years:", library.get_titles_between_years(2008, 2010))
        print("Most common year:", library.get_most_common_year())

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

    # Test error cases:
    try:
        library = MovieLibrary(MOVIE_JSON_FILE)

        print("\n--- Testing Error Cases ---\n")

        # Remove a no existent movie
        print("Removing non-existent movie:")
        try:
            library.remove_movie("Non Existent Movie")
        except MovieNotFoundError as e:
            print(e)

        # Update a no existent movie
        print("\nUpdating non-existent movie:")
        try:
            library.update_movie("Non Existent Movie", year=2025)
        except MovieNotFoundError as e:
            print(e)
            
        # Add a movie with a incorrect year
        print("\nAdding a movie with invalid year:")
        try:
            library.add_movie("Future Movie", "A. Director", 3000, ["Sci-Fi"])
        except ValueError as e:
            print(e)

    except FileNotFoundError as e:
        print(e)
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()