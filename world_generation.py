import noise
import numpy as np

from Cell import Cell
from TerrainType import TerrainType


class WorldGeneration:

    shape = (100,100)
    scale = 25.0
    octaves = 6
    persistence = 0.5
    lacunarity = 2.0

    def generate_noise_map(self):
        noise_map = np.zeros(self.shape)
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                noise_map[i][j] = noise.pnoise2(i / self.scale,
                                               j / self.scale,
                                               octaves=self.octaves,
                                               persistence=self.persistence,
                                               lacunarity=self.lacunarity,
                                               repeatx=100,
                                               repeaty=100,
                                               base=0)
        return noise_map;

    def generate_game_world(self):
        noise_map = self.generate_noise_map()
        world = []
        row_counter = 0
        for row in noise_map:
            world_row = []
            cell_counter = 0
            for cell in row:
                terrain_type = None
                if cell < -0.2:
                    terrain_type = TerrainType.WATER
                elif cell < -0.1:
                    terrain_type = TerrainType.SAND
                elif cell < 0.2:
                    terrain_type = TerrainType.GRASS
                elif cell < 0.6:
                    terrain_type = TerrainType.DIRT
                elif cell < 1:
                    terrain_type = TerrainType.ROCK
                world_row.append(Cell(terrain_type, (cell_counter, row_counter)))
                cell_counter += 1
            world.append(world_row)
            row_counter += 1
        return world