class Circle:

    def __init__(self, color, radius=5):
        self.radius = radius
        self.color = color


small_circle = Circle('Green')
print(small_circle.radius)
print(small_circle.color)
big_circle = Circle('Yellow', 25)
print(big_circle.radius)
print(big_circle.color)
medium_circle = Circle('White', radius=15)
print(medium_circle.radius)
print(medium_circle.color)
