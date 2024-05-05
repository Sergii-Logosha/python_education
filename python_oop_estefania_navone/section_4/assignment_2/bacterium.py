class Bacterium:

    def __init__(self, bacteria_type, shape, protection, life_counter, x, y, poisonous=False):
        self.bacteria_type = bacteria_type
        self.shape = shape
        self.protection = protection
        self.life_counter = life_counter
        self.poisonous = poisonous
        self.x = x
        self.y = y


bacillus_subtilis = Bacterium('Bacillus Subtilis', 'bacilli', 'low', 10, 3, 1)
staphylococcus = Bacterium('Staphylococcus', 'cocci', 'high', 10, 10, 10, poisonous=True)
escherichia_coli = Bacterium('Escherichia Coli', 'bacilli', 'middle', 10, 1, 9)
