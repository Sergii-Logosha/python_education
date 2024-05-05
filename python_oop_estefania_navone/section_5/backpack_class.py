class Backpack:

    max_num_items = 10

    def __init__(self):
        self.items = []


first_backpack = Backpack()
second_backpack = Backpack()

print(first_backpack.max_num_items)
print(second_backpack.max_num_items)
print(Backpack.max_num_items)
