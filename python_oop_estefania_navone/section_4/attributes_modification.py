class Circle:

    def __init__(self, radius, color):
        self.radius = radius
        self.color = color


blue_circle = Circle(5, 'Blue')
black_circle = Circle(10, 'Black')

print(blue_circle.radius)
print(blue_circle.color)
print(black_circle.radius)
print(black_circle.color)

black_circle.radius = 30
blue_circle.color = 'Red'

print(black_circle.radius)
print(blue_circle.color)
