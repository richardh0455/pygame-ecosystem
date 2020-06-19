from random import randint

from Animal import Animal
from Need import Need
from Needs import Needs
from RelationalNeed import RelationalNeed


class Fox(Animal):

    def __init__(self, starting_cell, gender):
        color = (245,172,75)
        # gender = Animal.genders[randint(0,1)]
        attraction = ("male", "female")[gender == "male"]
        needs = [Need(*Needs.WATER.value), Need(*Needs.SLEEP.value), RelationalNeed(*Needs.SEX.value, {"species": type(self), "gender": attraction})]
        super().__init__(color,needs, starting_cell, gender, 525600)



