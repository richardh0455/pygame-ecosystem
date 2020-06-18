

class Need:
    name = ""
    rate_of_decline = 1
    level = 100
    max_level = 100
    satisfied_terrain_type = None
    refresh_rate = 1

    def __init__(self, name, level, refresh_rate, rate_of_decline, satisfied_terrain_type):
        self.name = name
        self.level = level
        self.max_level = level
        self.refresh_rate = refresh_rate
        self.rate_of_decline = rate_of_decline
        self.satisfied_terrain_type = satisfied_terrain_type

    def cell_satisfies_need(self, cell):
        return cell.terrainType == self.satisfied_terrain_type

    def refresh_need(self):
        self.level = min(self.refresh_rate + self.level, self.max_level)

    def decline_need(self):
        self.level -= self.rate_of_decline
