import pygame
from random import *
import time


blue = (113,177,227)
white =(255,255,255) # valeur max = 255
pygame.init()

surfaceW = 800
surfaceH = 500
ballonW = 50
ballonH = 66
nuageW = 300
nuageH = 300
surface = pygame.display.set_mode((surfaceW,surfaceH))
pygame.display.set_caption("Ballon volant")
clock = pygame.time.Clock()

img = pygame.image.load('Ballon01.png')
img_nuage01 = pygame.image.load ('NuageHaut.png')
img_nuage02 = pygame.image.load ('NuageBas.png')

def score(compte):
    police = pygame.font.Font('BradBunR.ttf,16')
    texte = police.render("score :  + str(compte), True, white")
    surface.blit(texte, [10,0])

def nuage(x_nuage, y_nuage, espace):
    surface.blit (img_nuage01, (x_nuage, y_nuage))
    surface.blit (img_nuage02, (x_nuage, y_nuage + nuageW + espace))



def rejoue_ou_quitte():
    for event in pygame.event.get ([pygame.KEYDOWN, pygame.KEYUP, pygame.QUIT]):
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        elif event.type == pygame.KEYUP :
            continue
        return event.key
    return None


def createxteobj(texte, police):
    texte_surface = police.render(texte, True, white)
    return texte_surface, texte_surface.get_rect()


def message(texte):
    gros_texte = pygame.font.Font('BradBunR.ttf', 150)
    petit_texte = pygame.font.Font('BradBunR.ttf', 20)

    gros_textesurface, gros_texterect = createxteobj (texte, gros_texte)
    gros_texterect.center = surfaceW / 2, (surfaceH / 2) - 50
    surface.blit(gros_textesurface, gros_texterect)

    petit_textesurface, petit_texterect = createxteobj ("appuyez sur une touche pour continuer", petit_texte)
    petit_texterect.center = surfaceW / 2, (surfaceH / 2) + 50
    surface.blit(petit_textesurface, petit_texterect)

    pygame.display.update()
    time.sleep(2)


    while rejoue_ou_quitte() == None :
        clock.tick(30)
    principale()




def game_over_message():
    message("perdu")


def ballon (x,y,image):
    surface.blit(image, (x,y))


def principale():
    x = 150
    y = 200
    y_mouvement =0

    x_nuage = surfaceW
    y_nuage = randint(-300, 20)
    espace = ballonH*3
    nuage_vitesse = 6

    score_actuel = 0
    game_over = False
    while not game_over :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_UP :
                    y_mouvement = -5
            if event.type == pygame.KEYUP :
                y_mouvement = 5

        y += y_mouvement

        surface.fill(blue)
        ballon(x,y,img)

        nuage(x_nuage, y_nuage, espace)

        score(score_actuel)

        x_nuage -= nuage_vitesse

        pygame.display.update()



        if y > surfaceH - 40 or y < -10 :
            game_over_message()

        if x + ballonW >  x_nuage +20:
            if y < y_nuage + nuageH -50 :
                if x-ballonW < x_nuage + nuageW -10 :
                    game_over_message()

        if x + ballonW > x_nuage +20 :
            if y + ballonH > y_nuage + nuageH + espace +50:
                if x-ballonW < x_nuage + nuageW -10:
                    game_over_message()

        if x_nuage < (-1 * nuageW) :
            x_nuage = surfaceW
            y_nuage = randint(-300, 20)

        if x_nuage < (x-nuageW) < x_nuage + nuage_vitesse :
            score_actuel += 1

        clock.tick(30)

principale()
pygame.quit()
quit()
