from Animal import Animal


class Carcass(Animal):

    level = 100
    rate_of_decay = 2

    def __init__(self, animal, cell):
        super().__init__((0,0,0), None, cell, animal.gender, 0)

    def rot(self):
        self.level -= self.rate_of_decay

    def has_rotted(self):
        return self.level <= 0

