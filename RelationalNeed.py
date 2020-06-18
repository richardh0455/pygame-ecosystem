from Need import Need


class RelationalNeed(Need):
    criteria = {"species": None}
    def __init__(self, name, level, refresh_rate, rate_of_decline, criteria):
        super().__init__(name, level, refresh_rate, rate_of_decline, None)
        self.criteria = criteria

    def cell_satisfies_need(self, cell):
        animal_satisfies_criteria = next((animal for animal in cell.animals if type(animal) == self.criteria["species"] and (self.criteria["gender"] is None or animal.gender == self.criteria["gender"])), None)
        return animal_satisfies_criteria is not None

    #def add_criteria(self, criterion):
    #    self.criteria[criterion[0]] = criterion[1]

    #def add_gender_criteria(self, gender_value):
    #    self.add_criteria(("gender", gender_value))