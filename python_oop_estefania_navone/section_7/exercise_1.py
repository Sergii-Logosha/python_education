class Movie:

    def __init__(self, title, rating):
        self._title = title
        self.rating = rating

    def get_title(self):
        return self._title


movie = Movie('The Godfather', 4.9)

print(movie.get_title())
