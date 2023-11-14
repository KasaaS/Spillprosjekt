import pygame
from spiller import Spiller
from boss import Boss
from tile import Tile


# 1. Oppsett
pygame.init()
BREDDE = 800
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()


spiller = Spiller("bilder/spiller.png", 0.15, 5, "spiller", BREDDE, HOYDE)
boss = Boss("Bilder/boss.png", 0.35, 100, "boss", BREDDE, HOYDE)

dx = 0
dy = 0



lengde_brett = 4
bredde_brett = 7
brett_x = 220
brett_y = 300
brett = []

for i in range(0,lengde_brett):
    for j in range(0,bredde_brett):
        brett.append(Tile("bilder/tile.png", 1.5, brett_x + j*50, brett_y + i*50))
        

while True:
    # 2. Håndter input
    for hendelse in pygame.event.get():
        if hendelse.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        
        if hendelse.type == pygame.KEYDOWN:
            if hendelse.key == pygame.K_LEFT or hendelse.key== pygame.K_a:
                spiller.flytt(-1, 0)
            if hendelse.key == pygame.K_RIGHT or hendelse.key== pygame.K_d:
                spiller.flytt(1, 0)
            if hendelse.key == pygame.K_UP or hendelse.key== pygame.K_w:
                spiller.flytt(0, -1)
            if hendelse.key == pygame.K_DOWN or hendelse.key== pygame.K_s:
                spiller.flytt(0, 1)

        
    # 3. Oppdater spill

    # 4. Tegn
    vindu.fill("black")

    for i in range(len(brett)):
        brett[i].tegn(vindu)

    spiller.tegn(vindu)
    boss.tegn(vindu)
    

    pygame.display.flip()
    klokke.tick(FPS)