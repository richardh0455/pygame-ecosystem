from random import randint


class Animal:
    def __init__(self, color, speed):
        self.gender = randint(1, 2)
        self.color = color
        self.location = (0,0)
        self.speed = speed

    def get_next_move(self, boundaries):
        valid_moves = []
        if self.location[0] != boundaries[0]:
            valid_moves.append("W")
        if self.location[0] != boundaries[2]:
            valid_moves.append("E")
        if self.location[1] != boundaries[1]:
            valid_moves.append("N")
        if self.location[1] != boundaries[3]:
            valid_moves.append("S")

        return valid_moves[randint(0, len(valid_moves) - 1)]

    def update_location(self, next_move, cell_size):
        if next_move == "N":
            self.location = (self.location[0], self.location[1] - (cell_size * self.speed))
        elif next_move == "S":
            self.location = (self.location[0], self.location[1] + (cell_size * self.speed))
        elif next_move == "W":
            self.location = (self.location[0] - (cell_size * self.speed), self.location[1])
        elif next_move == "E":
            self.location = (self.location[0] + (cell_size * self.speed), self.location[1])
        print(self.location)
