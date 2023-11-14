from figur import Figur

class Tile(Figur):
    def __init__(self, bildesti: str, størrelse: int, x: int, y: int):
        super().__init__(bildesti, størrelse)

        self.ramme.x = x
        self.ramme.y = y

