from enum import Enum


class TerrainType(Enum):
    GRASS = (1, 166, 17)
    WATER = (42, 157, 244)
    DIRT = (97, 51, 24)
    SAND = (219, 202, 105)
    ROCK = (169, 161, 140)



    @staticmethod
    def list():
        return list(TerrainType)