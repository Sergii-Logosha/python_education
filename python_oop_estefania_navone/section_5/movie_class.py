class Movie:

    ids_counter = 0

    def __init__(self, title, year):
        self.title = title
        self.year = year
        self.id = Movie.ids_counter

        Movie.ids_counter += 1


film_1 = Movie("The Hobbit", "1999")
film_2 = Movie("Titanic", "2000")

print(film_1.id)
print(film_2.id)
