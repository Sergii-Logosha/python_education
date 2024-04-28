class Backpack:

    def __init__(self, size, color):
        self.items = []
        self.size = size
        self.color = color


old_backpack = Backpack('Medium', 'Black')
old_backpack.items = ['pen', 'notebook']
print(old_backpack.items)
