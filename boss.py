import pygame
from figur import Figur

class Boss(Figur):
    def __init__(self, bildesti: str, størrelse: int, liv: int, navn: str, vindu_bredde: int, vindu_høyde: int):
        super().__init__(bildesti, størrelse)


        self.ramme.centerx = vindu_bredde / 2       # Setter spilleren i startposisjon
        self.ramme.top = 60

        self.liv = liv
        self.navn = navn


    def mist_liv(self):
        if self.navn == "boss":
            self.liv -= 5
        else:
            self.liv -= 1

    
