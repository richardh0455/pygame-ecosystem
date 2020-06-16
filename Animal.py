from random import randint
import math
from TerrainType import TerrainType


class Animal:
    def __init__(self, color):
        self.gender = randint(1, 2)
        self.color = color
        ## location is (x,y)
        self.location = (0,0)
        self.needs = {'water': 100, 'sleep': 100}
        self.sight_radius = 20
        self.objective= None

    def get_next_objective(self):
        return min(self.needs.items(), key=lambda x: x[1])[0]

        ##TODO: Foxes can't swim
    def get_next_move(self, cells):
        if(self.objective is None):
                self.objective = self.get_next_objective()
                print("Next Objective is: "+self.objective)
        objective_location = self.identify_objective_location(cells, self.objective)
        valid_moves = self.get_valid_moves(cells)
        next_move = self.identify_best_move(valid_moves, objective_location)
        return next_move

    def execute_objective(self):
        self.needs[self.objective] = 100
        self.objective = None


    def identify_best_move(self, valid_moves, objective_location):
        if objective_location is None:
            ##Can't see the objective, can't stand still
            valid_moves.remove("O")
            return valid_moves[randint(0, len(valid_moves) - 1)]
        else:
            return min(valid_moves, key = lambda move: self.get_distance(self.get_location(move), objective_location))

    def identify_objective_location(self, cells, objective):
        min_x = max(self.location[0] - self.sight_radius, 0)
        max_x = min(self.location[0] + self.sight_radius, len(cells[0]))

        min_y = max(self.location[1] - self.sight_radius, 0)
        max_y = min(self.location[1] + self.sight_radius, len(cells))

        potential_locations = []

        y = min_y
        while y < max_y:
            x = min_x
            while x < max_x:
                if self.cell_satisfies_objective(cells[y][x], objective):
                    potential_locations.append(((x,y), self.get_distance(self.location, (x,y))))
                x += 1
            y += 1
        if len(potential_locations) == 0:
            return None
        else:
            return min(potential_locations, key = lambda t: t[1])[0]


    def get_distance(self, location1, location2):
        return math.sqrt(((location1[0]-location2[0])**2)+((location1[1]-location2[1])**2))

    def cell_satisfies_objective(self, cell, objective):
        return (objective == "water" and cell.terrainType == TerrainType.WATER) or (objective == "sleep" and cell.terrainType == TerrainType.GRASS)

    def get_valid_moves(self, cells):
        boundaries = (0, 0, len(cells[0]), len(cells))
        valid_moves = ["O"]
        if self.location[0] != boundaries[0]:
            valid_moves.append("W")
        if self.location[0] != boundaries[2]:
            valid_moves.append("E")
        if self.location[1] != boundaries[1]:
            valid_moves.append("N")
        if self.location[1] != boundaries[3]:
            valid_moves.append("S")
        return valid_moves

    def update_location(self, next_move):
        ##Reduce the needs by 1 each move the animal makes
        for k, v in self.needs.items(): self.needs[k] = v-1
        if next_move == 'O':
            self.execute_objective()
        else:
            self.location = self.get_location(next_move)


    def get_location(self, next_move):
        if next_move == "N":
            return (self.location[0], self.location[1] - 1)
        elif next_move == "S":
            return (self.location[0], self.location[1] + 1)
        elif next_move == "W":
            return (self.location[0] - 1, self.location[1])
        elif next_move == "E":
            return (self.location[0] + 1, self.location[1])
        elif next_move == "O":
            return self.location

