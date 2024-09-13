class Movie:

    def __init__(self, title, rating):
        self.title = title
        self._rating = rating

    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, new_rating):
        if isinstance(new_rating, float) and 1.0 < new_rating < 5.0:
            self._rating = new_rating
        else:
            print('Value for the rating is not valid')


my_movie = Movie('Titanic', 4.4)
print(my_movie.rating)
my_movie.rating = 4.5
print(my_movie.rating)
my_movie.rating = -4.2
print(my_movie.rating)
