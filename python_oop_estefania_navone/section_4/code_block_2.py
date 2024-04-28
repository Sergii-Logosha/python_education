class Circle:

    def __init__(self, radius):
        self.radius = radius
        self. color = 'Blue'


class Rectangle:

    def __init__(self, length, width):
        self.length = length
        self.width = width


class Movie:

    def __init__(self, title, year, language, rating):
        self.title = title
        self.year = year
        self.language = language
        self.rating = rating


my_favourite_movie = Movie('Titanic', 1999, 'English', 5)
your_favourite_movie = Movie('Die Hard', 1995, 'English', 4.6)

print('My favourite movie is: ')
print(my_favourite_movie.title)
print(my_favourite_movie.year)
print(my_favourite_movie.language)
print(my_favourite_movie.rating)
print()
print('Your favourite movie is: ')
print(your_favourite_movie.title)
print(your_favourite_movie.year)
print(your_favourite_movie.language)
print(your_favourite_movie.rating)

