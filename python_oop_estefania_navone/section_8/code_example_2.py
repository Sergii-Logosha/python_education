class Player:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move_up(self, y=5):
        self.y += y

    def move_down(self, y=5):
        self.y -= y

    def move_right(self, x=5):
        self.x += x

    def move_left(self, x=5):
        self.x -= x


bumblebee = Player(5, 5)

print(bumblebee.y)
bumblebee.move_up()
print(bumblebee.y)
