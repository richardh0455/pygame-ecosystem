from enum import Enum

from Need import Need
from TerrainType import TerrainType


class Needs(Enum):
    WATER = ("Water", 288, 144, 1, TerrainType.WATER)
    SLEEP = ("Sleep", 288, 3, 1, TerrainType.GRASS)
    SEX = ("Sex", 2016, 2016, 1)


    @staticmethod
    def list():
        return list(Needs)