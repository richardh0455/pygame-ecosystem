class Cell:

    def __init__(self, terrainType, location):
        self.location = location
        self.terrainType = terrainType
        self.animals = []

    def setTerrain(self, terrainType):
        self.terrainType = terrainType

    def getTerrain(self):
        return self.terrainType

    def add_animal(self, animal):
        self.animals.append(animal)

    def remove_animal(self, animal):
        self.animals.remove(animal)

