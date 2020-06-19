from operator import attrgetter
from random import randint
import math

from TerrainType import TerrainType


class Animal:
    genders = ["male", "female"]
    def __init__(self, color, needs, starting_cell, gender, lifespan):
        self.gender = gender
        self.age = 0
        self.lifespan = lifespan
        self.color = color
        ## location is (x,y)
        self._location = starting_cell.location
        starting_cell.add_animal(self)
        self._needs = needs
        self._sight_radius = 20
        self._objective= None

    def increase_age(self):
        self.age += 1

    def is_dead(self):
        return self.age >= self.lifespan or min(self._needs, key=attrgetter('level')).level <= 0

    def move(self, cells):
        next_move = self.__get_next_move(cells)
        self.__update_location(next_move, cells)
        print("Needs Are:")
        for need in self._needs:
            print(need.name + " : " + str(need.level))

        ##TODO: Foxes can't swim
    def __get_next_move(self, cells):
        if(self._objective is None):
                self._objective = self.__get_next_objective()
        objective_location = self.__find_objective_location(cells, self._objective)
        valid_moves = self.__get_valid_moves(cells)
        next_move = self.__find_best_move(valid_moves, objective_location)
        return next_move

    def __update_location(self, next_move, cells):
        ##Reduce the needs by 1 each move the animal makes
        needs = self._needs.copy()
        if next_move == 'O':
            needs.remove(self._objective)
            self.__execute_objective()
        else:
            cells[self._location[1]][self._location[0]].remove_animal(self)
            self._location = self.__get_location(next_move)
            cells[self._location[1]][self._location[0]].add_animal(self)

        for need in needs: need.decline_need()

    def __get_next_objective(self):
        ##Find the need with the lowest value
        return min(self._needs, key=attrgetter('level'))


    def __execute_objective(self):
        self._objective.refresh_need()
        self._objective = self.__get_next_objective()

    def __find_best_move(self, valid_moves, objective_location):
        if objective_location is None:
            # Can't see the objective, can't stand still
            valid_moves.remove("O")
            # Move in a random direction
            return valid_moves[randint(0, len(valid_moves) - 1)]
        else:
            # Find the move that would take us closer to the objective
            return min(valid_moves, key = lambda move: self.__get_distance(self.__get_location(move), objective_location))

    def __find_objective_location(self, cells, objective):
        min_x = max(self._location[0] - self._sight_radius, 0)
        max_x = min(self._location[0] + self._sight_radius, len(cells[0]))

        min_y = max(self._location[1] - self._sight_radius, 0)
        max_y = min(self._location[1] + self._sight_radius, len(cells))

        potential_locations = []

        y = min_y
        while y < max_y:
            x = min_x
            while x < max_x:
                if self.__cell_satisfies_objective(cells[y][x], objective):
                    potential_locations.append(((x,y), self.__get_distance(self._location, (x, y))))
                x += 1
            y += 1
        if len(potential_locations) == 0:
            return None
        else:
            return min(potential_locations, key = lambda t: t[1])[0]

    def __get_distance(self, location1, location2):
        return math.sqrt(((location1[0]-location2[0])**2)+((location1[1]-location2[1])**2))

    def __cell_satisfies_objective(self, cell, objective):
        return objective.cell_satisfies_need(cell)

    def __get_valid_moves(self, cells):
        boundaries = (0, 0, len(cells[0]), len(cells))
        valid_moves = ["O"]
        if self._location[0] != boundaries[0]:
            valid_moves.append("W")
        if self._location[0] != boundaries[2]:
            valid_moves.append("E")
        if self._location[1] != boundaries[1]:
            valid_moves.append("N")
        if self._location[1] != boundaries[3]:
            valid_moves.append("S")
        return valid_moves

    def __get_location(self, next_move):
        if next_move == "N":
            return (self._location[0], self._location[1] - 1)
        elif next_move == "S":
            return (self._location[0], self._location[1] + 1)
        elif next_move == "W":
            return (self._location[0] - 1, self._location[1])
        elif next_move == "E":
            return (self._location[0] + 1, self._location[1])
        elif next_move == "O":
            return self._location

