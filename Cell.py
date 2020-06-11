class Cell:

    def __init__(self, terrainType):
        self.data = []
        self.terrainType = terrainType

    def setTerrain(self, terrainType):
        self.terrainType = terrainType

    def getTerrain(self):
        return self.terrainType

