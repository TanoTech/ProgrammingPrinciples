import streamlit as st

from constant.config import MOVIE_JSON_FILE
from constant.constants import CURRENT_YEAR
from entities.movie_library import MovieLibrary


try:
    movie_library = MovieLibrary(MOVIE_JSON_FILE)
    st.success("Movie library loaded successfully!")
except FileNotFoundError:
    st.error("Movie JSON file not found.")

st.sidebar.title("Movie Library")
options = st.sidebar.radio("Choose an option:", ["Add Movie", "View Movies", "Update Movie", "Delete Movie", "Search"])

if options == "Add Movie":
    st.header("Add a New Movie")
    with st.form("add_movie_form"):
        title = st.text_input("Title")
        director = st.text_input("Director")
        year = st.number_input("Year", min_value=1895, max_value=CURRENT_YEAR, step=1)
        genres = st.text_input("Genres").split(',')
        submit = st.form_submit_button("Add Movie")
    
    if submit:
        try:
            movie_library.add_movie(title, director, int(year), genres)
            st.success("Movie added successfully!")
        except Exception as e:
            st.error(f"Failed to add movie: {e}")

elif options == "View Movies":
    st.header("Movie List")
    movies = movie_library.get_movies()
    if movies:
        for movie in movies:
            st.write(movie)
    else:
        st.info("No movies found in the library.")

elif options == "Update Movie":
    st.header("Update a Movie")
    movie_titles = movie_library.get_movie_titles()
    selected_movie = st.selectbox("Select a movie to update:", movie_titles)

    if selected_movie:
        with st.form("update_movie_form"):
            director = st.text_input("New Director (leave blank to keep current)")
            year = st.text_input("New Year (leave blank to keep current)")
            genres = st.text_input("New Genres ( leave blank to keep current)").split(',')
            submit = st.form_submit_button("Update Movie")
        
        if submit:
            try:
                movie_library.update_movie(selected_movie, director, int(year) if year else None, genres if genres else None)
                st.success(f"Movie '{selected_movie}' updated successfully!")
            except Exception as e:
                st.error(f"Failed to update movie: {e}")

elif options == "Delete Movie":
    st.header("Delete a Movie")
    movie_titles = movie_library.get_movie_titles()
    selected_movie = st.selectbox("Select a movie to delete:", movie_titles)
    
    if st.button("Delete Movie"):
        try:
            movie_library.remove_movie(selected_movie)
            st.success(f"Movie '{selected_movie}' deleted successfully!")
        except Exception as e:
            st.error(f"Failed to delete movie: {e}")

elif options == "Search":
    st.header("Search Movies")
    search_by = st.selectbox("Search by:", ["Title ", "Year", "Genre", "Director"])
    
    if search_by == "Title":
        substring = st.text_input("Enter titke:")
        if st.button("Search"):
            results = movie_library.get_movies_by_title_substring(substring)
            if results:
                for movie in results:
                    st.write(movie)
            else:
                st.info("No movies found.")

    elif search_by == "Year":
        year = st.number_input("Enter year:", min_value=1895, max_value=CURRENT_YEAR, step=1)
        if st.button("Search"):
            results = movie_library.get_movies_by_year(int(year))
            if results:
                for movie in results:
                    st.write(movie)
            else:
                st.info("No movies found.")

    elif search_by == "Genre":
        genre = st.text_input("Enter genre:")
        if st.button("Search"):
            results = movie_library.get_movies_by_genre(genre)
            if results:
                for movie in results:
                    st.write(movie)
            else:
                st.info("No movies found.")

    elif search_by == "Director":
        director = st.text_input("Enter director:")
        if st.button("Search"):
            count = movie_library.count_movies_by_director(director)
            st.write(f"Movies directed by {director}: {count}")
