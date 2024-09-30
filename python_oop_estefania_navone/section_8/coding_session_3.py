class Backpack:

    def __init__(self):
        self._items = []

    @property
    def items(self):
        return self._items

    def add_items(self, items):
        for item in items:
            self.add_item(item)

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

my_backpack.show_items()
my_backpack.add_items(['Watter Bottle', 'Candy', 'Sandwich'])
my_backpack.show_items()


