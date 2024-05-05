class Circle:

    radius = 5

    def __init__(self, color):
        self.color = color


circle_1 = Circle('red')
circle_2 = Circle('blue')

print(circle_1.radius)
print(circle_2.radius)
print(Circle.radius)

Circle.radius = 10

print(circle_1.radius)
print(circle_2.radius)
print(Circle.radius)
