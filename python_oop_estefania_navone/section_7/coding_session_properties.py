class Circle:

    VALID_COLORS = ('Red', 'Green', 'Yellow')

    def __init__(self, radius, color):
        self._radius = radius
        self._color = color

    def get_radius(self):
        return self._radius

    def set_radius(self, new_radius):
        if isinstance(new_radius, int) and new_radius > 0:
            self._radius = new_radius
        else:
            print('Value for the radius is not valid')

    radius = property(get_radius, set_radius)

    def get_color(self):
        return self._color

    def set_color(self, new_color):
        if new_color in Circle.VALID_COLORS:
            self._color = new_color
        else:
            print('Value for the color is not valid')

    color = property(get_color, set_color)


little_circle = Circle(29, 'Red')

print(little_circle.radius)
little_circle.radius = 0
print(little_circle.radius)
little_circle.radius = 4
print(little_circle.radius)

print(little_circle.color)
little_circle.color = 'Yellow'
print(little_circle.color)

little_circle.color = 'Black'
print(little_circle.color)
