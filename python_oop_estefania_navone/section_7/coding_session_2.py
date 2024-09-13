class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_item):
        if isinstance(new_item, str):
            self._items.append(new_item)
        elif isinstance(new_item, list):
            self._items.extend(new_item)
        else:
            print('Enter valid value for item')


my_backpack = Backpack()
print(my_backpack.items)
my_backpack.items = 'Watter bottle'
print(my_backpack.items)
my_backpack.items = ['Pen', 'Notebook']
print(my_backpack.items)
my_backpack.items = {'Pencil box': 'Red'}
print(my_backpack.items)
