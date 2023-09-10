import pygame
import monitor

nombreDePipes = 0

pygame.init()
# ----------------------------
# les images pour notre jeux
# ----------------------------
background = pygame.image.load("sprites/background-night.png")
sol = pygame.image.load("sprites/base.png")
clock = pygame.time.Clock()

SCREEN_WIDTH, SCREEN_HEIGHT = background.get_size()

double_ground = pygame.Surface((2 * SCREEN_WIDTH, sol.get_height()))
double_ground.blit(sol, (0, 0))
double_ground.blit(sol, (SCREEN_WIDTH, 0))
bird = pygame.image.load("sprites/bluebird-midflap.png")


screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
positionsol = 0

positionbirdY = SCREEN_HEIGHT / 2 - bird.get_height() / 2

G = 0.2
v = 0
F = 0
pipey = 0
vpipe = 1

start = True

while start:

    F = 0

    # ----------------------------
    # GESTION DES EVENEMENTS DE LA FENETRE
    # ----------------------------
    for event in pygame.event.get():
        # SI BOUTON CLOSE DE LA FENTRE ARRETER BOUCLE DE JEUX
        if event.type == pygame.QUIT:
            start = False
        elif event.type == pygame.KEYDOWN:
            print('key press')
            F = -4

    # ----------------------------
    # Boucle de calcul
    # ----------------------------
    # -----------------------------
    # calcul sur objet
    # -----------------------------
    # sol
    positionsol = positionsol - 1
    if positionsol <= -SCREEN_WIDTH:
        positionsol = 0
    # bird
    a = G + F
    v = v + a
    positionbirdY = positionbirdY + v

    if positionbirdY + bird.get_height() >= SCREEN_HEIGHT - sol.get_height():
        positionbirdY = SCREEN_HEIGHT - sol.get_height() - bird.get_height()

        v = 0

    for n in monitor.TPipes :
         n.calcul()


    # ---------------------------
    # MONITOR
    # ---------------------------

    monitor.GenerateurDePipe()



    # ---------------------------
    # END MONITOR
    # ---------------------------

    # AJOUT DES ELEMENTS
    # ajout du background
    screen.blit(background, (0, 0))
    # ajout du sol
    screen.blit(double_ground, (positionsol, SCREEN_HEIGHT - sol.get_height()))
    # ajout de l' oiseau
    screen.blit(bird, (SCREEN_WIDTH / 2 - bird.get_width() / 2, positionbirdY))

    # ajout du tube

    # afficher a  l' ecran

    for n in monitor.TPipes :
         n.display(screen)

    pygame.display.update()

    clock.tick(60)
