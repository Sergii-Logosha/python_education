class Circle:

    def __init__(self, radius):
        self._radius = radius

    def get_radius(self):
        return self._radius

    def set_radius(self, new_value):
        if isinstance(new_value, float) and new_value > 0:
            self._radius = new_value
        else:
            print('You are trying to enter not valid value')


simple_circle = Circle(5)
print(f'Circle radius is {simple_circle.get_radius()}')
simple_circle.set_radius(10)
print(f'Circle radius is {simple_circle.get_radius()}')
simple_circle.set_radius(2.5)
print(f'Circle radius is {simple_circle.get_radius()}')
simple_circle.set_radius(-3)
print(f'Circle radius is {simple_circle.get_radius()}')
