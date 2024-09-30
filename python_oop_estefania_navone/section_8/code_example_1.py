class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_diameter(self):
        print(f'Diameter: {self.radius * 2}')


the_circle = Circle(5)
the_circle.get_diameter()
