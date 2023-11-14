import pygame
from figur import Figur

class Spiller(Figur):
    def __init__(self, bildesti: str, størrelse: int, liv: int, navn: str, vindu_bredde: int, vindu_høyde: int):
        super().__init__(bildesti, størrelse)


        self.ramme.centerx = 394     # Setter spilleren i startposisjon
        self.ramme.bottom = 430

        self.liv = liv
        self.navn = navn


    def mist_liv(self):
        if self.navn == "boss":
            self.liv -= 5
        else:
            self.liv -= 1
            

    def flytt(self, dx: int, dy: int):
        self.ramme.x += dx*50
        self.ramme.y += dy*50

    
