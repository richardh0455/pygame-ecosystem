from Animal import Animal


class Fox(Animal):

    def __init__(self):
        color = (245,172,75)
        super().__init__(color)

    def get_next_move(self, boundaries):
        return super().get_next_move(boundaries)


