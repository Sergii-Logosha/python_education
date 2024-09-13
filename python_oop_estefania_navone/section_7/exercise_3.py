class Backpack:

    def __init__(self):
        self._items = []

    def get_items(self):
        return self._items

    def set_items(self, new_items):
        if isinstance(new_items, list):
            self._items = new_items
        else:
            print('Please, enter valid list of items')


black_backpack = Backpack()
print(f'Items in the backpack: {black_backpack.get_items()}')
black_backpack.set_items(['Water bottle', 'First Aid Kit', 'Knife'])
print(f'Items in the backpack: {black_backpack.get_items()}')
