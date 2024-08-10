class Movie:

    id_counter = 1

    def __init__(self, title, year, language, rating):
        self._id = Movie.id_counter
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating

        Movie.id_counter += 1


first_movie = Movie("Titanic", 1999, "English", 5.0)
second_movie = Movie("Birds", 2000, "English", 5.0)

print(first_movie._id)
print(second_movie.id)
