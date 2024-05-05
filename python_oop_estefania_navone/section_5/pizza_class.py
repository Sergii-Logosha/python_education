class Pizza:

    price = 5

    def __init__(self, size, type):
        self.size = size
        self.type = type


pizza1 = Pizza('large', 'Pepperoni')
pizza2 = Pizza('small', 'Havana')

print(Pizza.price)

Pizza.price = 1

print(Pizza.price)
