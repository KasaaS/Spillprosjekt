import pygame
from figur import Figur
from collider import Collider

class Spiller(Figur):
    def __init__(self, bildesti: str, størrelse: int, liv: int, vindu_bredde: int, vindu_høyde: int):
        super().__init__(bildesti, størrelse)


        self.ramme.centerx = 393     # Setter spilleren i startposisjon
        self.ramme.bottom = 435

        self.ramme_collide = self.bilde.get_rect()
        self.ramme_collide.height = self.ramme_collide.height/2
        self.ramme_collide.bottom = self.ramme.bottom

        self.liv = liv


        
    def flytt(self, dx: int, dy: int):

        self.ramme.x += dx*50
        if self.ramme.x <= 220:
            self.ramme.centerx = 243
        if self.ramme.x >= 557:
            self.ramme.centerx = 543
        

        self.ramme.y += dy*50
        if self.ramme.y <= 262:
            self.ramme.centery = 310
        if self.ramme.y >=430:
            self.ramme.centery = 460

        self.ramme_collide.center = self.ramme.center


    def mist_liv(self, navn: str):
        if navn == "boss":
            self.liv -= 5
        else:
            self.liv -= 1

    def få_liv(self):
        if self.liv < 5:
            self.liv += 1