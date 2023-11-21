import pygame
import random
from spiller import Spiller
from boss import Boss
from tile import Tile
from collider import Collider


# 1. Oppsett
pygame.init()
BREDDE = 800
HOYDE = 600
FPS = 60
vindu = pygame.display.set_mode((BREDDE, HOYDE))
klokke = pygame.time.Clock()
nivå = 1


pygame.display.set_caption("Planke")
font = pygame.font.SysFont("Arial", 32) # Skrifttype


spiller = Spiller("bilder/spiller.png", 0.1, 5, BREDDE, HOYDE)
boss = Boss("Bilder/boss.png", 0.35, 100, BREDDE, HOYDE)


boss_hjerte = Boss("Bilder/boss.png", 0.15, 100, 100, HOYDE)
spiller_hjerte = Collider("Bilder/hjerte.png", 0.05, 35, 150)


hjerte = Collider("bilder/hjerte.png", 0.04, 228 + random.randint(0,6)*50, 307 + random.randint(0,3)*50)

dx = 0
dy = 0



lengde_brett = 4
bredde_brett = 7
brett_x = 220
brett_y = 300

brett = []
angrep = []


FPS_teller = 0

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
    if FPS_teller > 300:
        FPS_teller = 0
        if len(angrep) <= 20:
          angrep.append(Collider("bilder/planke.png", 0.075, 230 + random.randint(0,6)*50, 302 + random.randint(0,3)*50))

    for i in range(len(angrep)):
        if spiller.ramme_collide.colliderect(angrep[i].ramme):
            spiller.mist_liv("spiller")
            angrep[i] = Collider("bilder/planke.png", 0.075, 230 + random.randint(0,6)*50, 302 + random.randint(0,3)*50)
            


    if spiller.ramme_collide.colliderect(hjerte.ramme):
            boss.mist_liv("boss")
            spiller.få_liv()
            hjerte = Collider("bilder/hjerte.png", 0.04, 228 + random.randint(0,6)*50, 307 + random.randint(0,3)*50)

            if boss.liv == 0:
                nivå += 1
                boss.liv = nivå*100

    
    if spiller.liv == 0:
        pygame.quit()
        raise SystemExit
    

    spiller_liv = font.render(str(spiller.liv), True, "black")
    boss_liv = font.render(str(boss.liv), True, "black")
    nivå_skrift = font.render(str(nivå), True, "black")
    level_skrift = font.render("Level", True, "black")



    # 4. Tegn
    vindu.fill("red")
    vindu.blit(boss_liv,(100,80))
    vindu.blit(spiller_liv,(100,150))
    vindu.blit(nivå_skrift,(130,220))
    vindu.blit(level_skrift,(40,220))

    for i in range(len(brett)):
        brett[i].tegn(vindu)

    for k in range(len(angrep)):
        angrep[k].tegn(vindu)


    spiller.tegn(vindu)
    boss.tegn(vindu)


    hjerte.tegn(vindu)
    boss_hjerte.tegn(vindu)
    spiller_hjerte.tegn(vindu)
    

    pygame.display.flip()
    klokke.tick(FPS)
    FPS_teller += 1