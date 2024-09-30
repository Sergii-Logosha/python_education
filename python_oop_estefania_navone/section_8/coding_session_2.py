class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_item(self, item):
        if isinstance(item, str):
            self._items.append(item)
        else:
            print('Provided item is not valid')

    def remove_item(self, item):
        if item in self._items:
            self._items.remove(item)
            return 1
        else:
            return 0

    def has_item(self, item):
        return item in self._items

    def show_items(self, is_sorted=False):
        if is_sorted:
            print(sorted(self._items))
        else:
            print(self._items)


my_backpack = Backpack()
my_backpack.add_item('Screwdriver')
my_backpack.add_item('Candy')
my_backpack.add_item('Water bottle')

print('Not Sorted:')
my_backpack.show_items()
print('Sorted:')
my_backpack.show_items(True)
