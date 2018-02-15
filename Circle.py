#!/usr/bin/python
#-*- coding: utf-8 -*-
import os
import random
import sys
import math
from math import *

import pygame
import pygame.gfxdraw
from pygame.locals import *

pygame.display.init()


WIDTH = 640
HEIGHT = 480
FPS = 30

WHITE = (254, 254, 254)
BLACK = (0, 0, 0)
BLUE = (54, 225, 243)
PURPLE = (141, 19, 250)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (247, 222, 15)
ROSE = (252, 2, 128)
GREY = (41, 41, 41)

colors = (BLUE, YELLOW, PURPLE, ROSE)

# initialisation de la fenetre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SwitchColor")
clock = pygame.time.Clock()  # fps

# background = pygame.image.load("Vue/Image/voielactee.jpg").convert()

# screen.blit(background,(0,0))


class Ball(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("Vue/Image/redball.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        # self.image = pygame.Surface((50,50))
        # self.image.fill(color)
        # self.image.fill(a)
        # self.image.set_alpha(128)
        # pygame.gfxdraw.filled_circle(self.image,25,25,25,RED)

    def jump(self):
        self.rect.y -= 40

    def update(self):  # gravite
        if self.rect.y < 410:
            self.rect.y += 2

TILE_SIZE = 75


class Grid():

    def __init__(self):
        self.grid = pygame.Surface([200, 200])
        self.grid.fill((0, 0, 0, 0))
        # self.grid.set_colorkey((0, 0, 0, 0))

    def draw(self):
        # DRAW TILE LINES -----------------------------------------------------
        grid_x = 0
        grid_y = 0
        for i in range(WIDTH // TILE_SIZE):
            pygame.draw.aaline(
                self.grid, WHITE, [grid_x, 0], [grid_x, HEIGHT])
            pygame.draw.aaline(
                self.grid, WHITE, [0, grid_x], [WIDTH, grid_y])
            grid_x += TILE_SIZE
            grid_y += TILE_SIZE
        # tile test
        pygame.draw.rect(
            screen, BLACK, (49 * TILE_SIZE, 34 * TILE_SIZE, TILE_SIZE, TILE_SIZE))
        print("bravo")
        screen.blit(self.grid, (0, 0))


class Arc(pygame.sprite.Sprite):

    def __init__(self, image, color, rect, start_angle, stop_angle, width):
        pygame.sprite.Sprite.__init__(self)
        self.i = 1
        self.color = color
        self.image = image
        # self.image.fill((0, 0, 0, 0))
        self.rect = rect
        self.rect.move_ip(rect.x, rect.y)
        self.update(start_angle, stop_angle, width)

    def update(self, start_angle, stop_angle, width):
        # self.image.fill((0, 0, 0, 0))
        pygame.draw.arc(
            self.image, self.color, self.rect, start_angle, stop_angle, width)
        pygame.draw.arc(
            self.image, self.color, self.rect, start_angle - 0.01, stop_angle + 0.01, width)
        self.rect.center = (100, 100)

    def draw(self):
        pass


class Star(pygame.sprite.Sprite):

    def __init__(self, rect):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "Vue/Image/star2.png").convert_alpha()
        self.rect = self.image.get_rect()  # correspond a la surface du cercle
        self.rect.move_ip(77, 80)  # permet de centrer l'etoile dans le
        # cercle
        self.mask = pygame.mask.from_surface(self.image)
        self.bool = False

    def update(self):
        pass

    def collide(self, player):
        if self.rect.colliderect(player):
            print("Collision Star")
        elif self.rect.contains(player.rect):
            print("Collision Star")
        elif self.rect.collidepoint(player.rect.center):
            print("Collision Star")
        else:
            pass


class Switch(pygame.sprite.Sprite):  # class du joueur

    def __init__(self, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(
            "Vue/Image/switch3.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, pos_y)
        self.mask = None
        self.pos_y = pos_y
        self.scroll = 0

    def udpdate(self):
        self.rect.center = (WIDTH / 2, self.pos_y + self.scroll)
        # self.rect.y = self.pos.y + self.scroll
        self.mask = pygame.mask.from_surface(self.image)

    def collide(self, player):
        """
        if pygame.sprite.collide_mask(player, self):
            player.color = random.choice(colors)
            print("collision avec le switch")
            self.image.fill((0, 0, 0, 0))
        """


class Circle(pygame.sprite.Sprite):  # TODO

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200, 200]).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill((0, 0, 0, 0))
        self.rect.y = 200

        self.i = 0  # vitesse de rotatio
        self.scroll = 0  # permet le scrolling

       # self.all_arcs = pygame.sprite.Group()

        # self.star = Star(self.rect)
        # self.rect = self.rect.clamp(self.star.rect)

        self.arc_1 = Arc(
            self.image, PURPLE, [self.rect.x, self.rect.y, self.rect.w, self.rect.h], 0 + self.i, pi / 2 + self.i, 15)
        self.arc_1 = Arc(
            self.image, PURPLE, [self.rect.x, self.rect.y, self.rect.w, self.rect.h], 0 + self.i, pi / 2 + self.i, 15)
        self.arc_1 = Arc(
            self.image, PURPLE, [self.rect.x, self.rect.y, self.rect.w, self.rect.h], 0 + self.i, pi / 2 + self.i, 15)
        self.arc_2 = Arc(
            self.image, YELLOW, self.rect, pi / 2 + self.i, pi + self.i, 16)
        self.arc_3 = Arc(
            self.image, BLUE, self.rect, pi + self.i, 3 * pi / 2 + self.i, 15)
        self.arc_4 = Arc(
            self.image, ROSE,  self.rect, 3 * pi / 2 + self.i, 2 * pi + self.i, 15)

        """
        self.all_arcs.add(self.arc_1)
        self.all_arcs.add(self.arc_2)
        self.all_arcs.add(self.arc_3)
        self.all_arcs.add(self.arc_4)
        """
        # self.all_arcs.add(self.star)
        # self.rect.center = (640 / 2, self.rect.y)
        self.rect.center = (640 / 2, 200)

        # self.all_arcs.draw(self.image)

        # self.update()

        # self.image.fill((0, 0, 0, 0))
        # self.image.fill((41, 41, 41))

    def dessiner_arc(self, image, color, rect, start_angle, stop_angle, width):

        for i in range(10):
            self.arc_1 = Arc(
                image, color, rect, start_angle, stop_angle, 40)

    def update(self):

        # self.all_arcs.clear(self.image, (41, 41, 41))
        # self.image.fill((0, 0, 0, 0))
        # self.image.fill((41, 41, 41))

        self.i += 0.02  # vitesse de rotation

        self.arc_1.update(0 + self.i, pi / 2 + self.i, 15)
        self.arc_1.update(0 + self.i, pi / 2 + self.i, 15)
        self.arc_2.update(pi / 2 + self.i, pi + self.i, 15)
        self.arc_3.update(pi + self.i, 3 * pi / 2 + self.i, 15)
        self.arc_4.update(3 * pi / 2 + self.i, 2 * pi + self.i, 15)

        self.all_arcs.draw(self.image)

        # self.rect.center = (640 / 2, self.rect.y + self.scroll)
        self.rect.center = (640 / 2, 200)

    def clear(self):
        self.all_arcs.empty()

        self.all_arcs.add(self.arc_1)
        self.all_arcs.add(self.arc_2)
        self.all_arcs.add(self.arc_3)
        self.all_arcs.add(self.arc_4)

    def draw(self, screen):
        screen.blit(self.image, (50, 50))


class Cercle(pygame.sprite.Sprite):  # TODO

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([200, 200]).convert_alpha()
        self.rect = self.image.get_rect()
        self.image.fill((0, 0, 0, 0))
        self.rect.y = 200

        self.i = 0  # vitesse de rotatio
        self.scroll = 0  # permet le scrolling

        self.all_arcs = pygame.sprite.Group()

        # self.star = Star(self.rect)
        # self.rect = self.rect.clamp(self.star.rect)

        self.arc_1 = Arc(
            self.image, PURPLE, self.rect, 0 + self.i, pi / 2 + self.i, 15)
        self.arc_1 = Arc(
            self.image, PURPLE, self.rect, 0 + self.i, pi / 2 + self.i, 15)
        self.arc_2 = Arc(
            self.image, YELLOW, self.rect, pi / 2 + self.i, pi + self.i, 15)
        self.arc_3 = Arc(
            self.image, BLUE, self.rect, pi + self.i, 3 * pi / 2 + self.i, 15)
        self.arc_4 = Arc(
            self.image, ROSE,  self.rect, 3 * pi / 2 + self.i, 2 * pi + self.i, 15)

        self.all_arcs.add(self.arc_1)
        self.all_arcs.add(self.arc_2)
        self.all_arcs.add(self.arc_3)
        self.all_arcs.add(self.arc_4)

        # self.all_arcs.add(self.star)
        # self.rect.center = (640 / 2, self.rect.y)
        self.rect.center = (640 / 2, 200)

        # self.all_arcs.draw(self.image)

        # self.update()

        # self.image.fill((0, 0, 0, 0))
        # self.image.fill((41, 41, 41))

    def update(self):

        # self.all_arcs.clear(self.image, (41, 41, 41))
        # self.image.fill((0, 0, 0, 0))
        # self.image.fill((41, 41, 41))

        self.i += 0.02  # vitesse de rotation

        self.arc_1.update(0 + self.i, pi / 2 + self.i, 15)
        self.arc_1.update(0 + self.i, pi / 2 + self.i, 15)
        self.arc_2.update(pi / 2 + self.i, pi + self.i, 15)
        self.arc_3.update(pi + self.i, 3 * pi / 2 + self.i, 15)
        self.arc_4.update(3 * pi / 2 + self.i, 2 * pi + self.i, 15)

        self.all_arcs.draw(self.image)

        # self.rect.center = (640 / 2, self.rect.y + self.scroll)
        self.rect.center = (640 / 2, 200)

    def clear(self):
        self.all_arcs.empty()

        self.all_arcs.add(self.arc_1)
        self.all_arcs.add(self.arc_2)
        self.all_arcs.add(self.arc_3)
        self.all_arcs.add(self.arc_4)

    def collisions(self, player):
        color = player.color
        if pygame.sprite.collide_mask(player, self.arc_1) and color != self.arc_1.color:
            print("Collision couleur PURPLE")
        elif pygame.sprite.collide_mask(player, self.arc_2) and color != self.arc_2.color:
            print("Collision couleur YELLOW")
        elif pygame.sprite.collide_mask(player, self.arc_3) and color != self.arc_3.color:
            print("Collision couleur BLUE")
        elif pygame.sprite.collide_mask(player, self.arc_4) and color != self.arc_4.color:
            print("Collision couleur ROSE")
        elif player.rect.y < self.star.rect.y + self.rect.y + 45 and self.star.bool == False:  # collision temporaire
            self.star.image.fill((0, 0, 0, 0))
            player.score += 1
            self.star.bool = True

        else:
            pass
            # self.star.collide(player)


class Ligne(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([1200, 50])
        self.rect = self.image.get_rect()

        self.w_green_1 = 426
        self.w_green_2 = 640
        self.w_red_1 = 0
        self.w_red_2 = 213
        self.w_blue_1 = 213
        self.w_blue_2 = 426

        self.speed = 2

        self.initialization()

    def initialization(self):
        self.image.fill((0, 0, 0, 0))

        pygame.draw.lines(
            self.image, BLUE, False, [[50, 50], [100, 100]], 6)
        """
        pygame.draw.lines(
            self.image, GREEN, False, [[self.w_green_1, 400], [self.w_green_2, 400]], 6)
        pygame.draw.lines(
            self.image, RED, False, [[self.w_red_1, 400], [self.w_red_2, 400]], 6)
        pygame.draw.lines(
            self.image, BLUE, False, [[self.w_blue_1, 400], [self.w_blue_2, 400]], 6)
        """
        self.rect.center = (0, 350)

    def update(self):
        # print("update ligne")
        self.initialization()

    def incremente(self, width):
        if width < 640:
            return width + 1
        # else:
         #   return 0

pygame.key.set_repeat(400, 30)

all_sprites = pygame.sprite.Group()  # permet de regrouper les sprites


def intro():
    intro = True
    intro_background = pygame.image.load("Vue/Image/planete1.jpg")
    screen.blit(intro_background, (0, 0))
    while intro:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                quit()
            else:
                if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
                    circle_loop()
                    intro = False
        pygame.display.flip()

    pygame.display.quit()
    quit()


def ligne(l):
    if l < 640:
        return l + 1
    else:
        return 0


def circle_loop():

    # rect_sc = screen.get_rect()
    # surf = pygame.Surface((200, 200)).convert_alpha()
    # surf.fill((0, 0, 0, 0))
    # rect = surf.get_rect()
    # pygame.draw.arc(surf, ROSE, rect, 0, 100, 15)
    # rect.center = (100, 200)

    # screen.blit(surf, (50, 50))

   # arc = Arc(screen, ROSE, 0, 100, 16)
    # cercle = Circle()
    end = False
    i = 0
    # grid = Grid()

    switch = Switch(100)
    carre = pygame.Surface([200, 200]).convert()
    rect1 = carre.get_rect()
    rect1.center = (200, 200)
    carre.fill(PURPLE)

    # ball = Ball()
    # ligne = Ligne()
    # cercle = Circle()
    all_sprites.add(switch)
   # all_sprites.add(cercle)
   # all_sprites.add(arc)
    # all_sprites.add(ligne)
    # all_sprites.add(cercle)

    A = 70
    angleDegre = 0
    angleRadian = pi * angleDegre / 180
    sina = sin(angleRadian)
    cosa = cos(angleRadian)

    angleDegre2 = 90
    angleRadian2 = pi * angleDegre2 / 180
    sina2 = sin(angleRadian2)
    cosa2 = cos(angleRadian2)

    angleDegre3 = 180
    angleRadian3 = pi * angleDegre3 / 180
    sina3 = sin(angleRadian3)
    cosa3 = cos(angleRadian3)

    angleDegre4 = 270
    angleRadian4 = pi * angleDegre4 / 180
    sina4 = sin(angleRadian4)
    cosa4 = cos(angleRadian4)
    # objet = Cercle(300,200,50,RED)

    coord = 75
    coord1 = 75
    coord2 = 75
    coord3 = 75

    # parametrage des lignes mutlicolor
    wgreen = 426
    wred = 0
    wblue = 213

    wgreen2 = 640
    wred2 = 213
    wblue2 = 426

    while not end:
        # Events
        try:
            for event in pygame.event.get():
                if event.type == QUIT:
                    end = True
                else:
                    if event.type == KEYDOWN:
                        if event.key == K_SPACE:
                            ball.jump()
                            # all_sprites.jump()

                        if event.key == K_q:
                            end = True
        except Exception:
            print("Erreur !")

        # print(circle.rect.x,circle.rect.y,circle.rect.height,circle.rect.width)

        # Update
        all_sprites.update()  # met a jour tous les sprites

        # Draw / render

        screen.fill((41, 41, 41))
        # screen.blit(background, (0, 0))
        all_sprites.draw(screen)  # affiche tous les sprites
        # grid.draw()
        # screen.blit(grid.grid, (0, 0))

        # cercle multicolor
        """
        pygame.draw.arc(screen, WHITE,[320, coord2, coord+i, coord1], 0+i, pi/2+i, 2)
        pygame.draw.arc(screen, GREEN,[320, coord2, coord+i, coord1], pi/2+i, pi+i, 2)
        pygame.draw.arc(screen, BLUE, [320 ,coord2, coord+i, coord1], pi+i,3*pi/2+i, 2)
        pygame.draw.arc(screen, RED,  [320, coord2, coord+i, coord1], 3*pi/2+i, 2*pi+i, 2)

        pygame.draw.arc(screen, WHITE,[100, coord2, coord, coord1], 0+i, pi/2+i, 10)
        pygame.draw.arc(screen, GREEN,[100, coord2, coord, coord1], pi/2+i, pi+i, 10)
        pygame.draw.arc(screen, BLUE, [100, coord2, coord, coord1], pi+i,3*pi/2+i, 10)
        pygame.draw.arc(screen, RED,  [100, coord2, coord, coord1], 3*pi/2+i, 2*pi+i, 10)
        """
        # i += 0.01
        # etoile = pygame.image.load(
        #    "Vue/Image/etoileArgent.png").convert_alpha()
        # screen.blit(etoile, (200, 200))

        # pygame.draw.arc(
        # screen, GREEN, [100, coord2, coord, coord1], (pi / 2) + i, pi + i,
        # 15)

        pygame.draw.arc(
            screen, GREEN, [100, 100, 100, 100], 0, 2, 15)

        pygame.draw.arc(
            screen, PURPLE, (400, 400, 200, 200), math.radians(0), math.radians(90), 15)
        pygame.draw.arc(
            screen, PURPLE, (400, 400 + 1, 200, 200), math.radians(0), math.radians(90), 15)
        """
        surf = pygame.Surface([1200, 50]).convert_alpha()

        line = pygame.draw.lines(
            screen, BLUE, False, [[50, 50], [100, 100]], 6)

        rec = pygame.Rect((0, 0), (100, 50))

        pygame.gfxdraw.box(surf, rec, WHITE)

        surf.blit(screen, (0, 0))

        """

        """
        if(bd != 0):
            B -= bd / 2
            D += bd / 2
        """

        """
        A = 300 + (A - 300) * cos(math.radians(i)) - \
            (B - 300) * sin(math.radians(i))
        B = 300 + (A - 300) * sin(math.radians(i)) + \
            (B - 300) * cos(math.radians(i))
        C = 300 + (C - 300) * cos(math.radians(i)) - \
            (D - 300) * sin(math.radians(i))
        D = 300 + (C - 300) * sin(math.radians(i)) + \
            (D - 300) * cos(math.radians(i))



        A = 300 + (A - 300) * cos(i * ((1 / pi) / 180)) - \
            (B - 300) * sin(i * ((1 / pi) / 180))
        B = 300 + (A - 300) * sin(i * ((1 / pi) / 180)) + \
            (B - 300) * cos(i * ((1 / pi) / 180))
        C = 300 + (C - 300) * cos(i * ((1 / pi) / 180)) - \
            (D - 300) * sin(i * ((1 / pi) / 180))
        D = 300 + (C - 300) * sin(i * ((1 / pi) / 180)) + \
            (D - 300) * cos(i * ((1 / pi) / 180))
        """
        angleRadian = pi * angleDegre / 180
        sina = sin(angleRadian)
        cosa = cos(angleRadian)

        angleRadian2 = pi * angleDegre2 / 180
        sina2 = sin(angleRadian2)
        cosa2 = cos(angleRadian2)

        angleRadian3 = pi * angleDegre3 / 180
        sina3 = sin(angleRadian3)
        cosa3 = cos(angleRadian3)

        angleRadian4 = pi * angleDegre4 / 180
        sina4 = sin(angleRadian4)
        cosa4 = cos(angleRadian4)

        Y = 250 + A * cosa - A * sina
        Z = 250 + A * sina + A * cosa

        X = 250 + A * cosa2 - A * sina2
        W = 250 + A * sina2 + A * cosa2

        S = 250 + A * cosa3 - A * sina3
        T = 250 + A * sina3 + A * cosa3

        F = 250 + A * cosa4 - A * sina4
        K = 250 + A * sina4 + A * cosa4

        pygame.draw.line(screen, YELLOW, (300, 300), (300, 300), 5)
        pygame.draw.line(screen, PURPLE, (Y, Z), (X, W), 15)
        pygame.draw.line(screen, YELLOW, (X, W), (S, T), 15)
        pygame.draw.line(screen, BLACK, (S, T), (F, K), 15)
        pygame.draw.line(screen, GREEN, (F, K), (Y, Z), 15)

        # pygame.draw.aalines(screen,PURPLE,True,[(Y-50,Z-50),(Y,Z),(Y+50,Z+50)])
        # pygame.draw.aalines(
        #    screen, PURPLE, True, [(Y, Z), (X, W)])

        # pygame.gfxdraw.line(screen, int(Y), int(
        #    Z - 6), int(X), int(W - 8), PURPLE)
        # pygame.gfxdraw.line(screen, int(Y), int(
        #    Z + 8), int(X), int(W + 6), PURPLE)

        img2 = pygame.image.load(
            "Vue/Image/switch3.png").convert_alpha()
        screen.blit(img2, (200, 200))

        angleDegre += 1
        angleDegre2 += 1
        angleDegre3 += 1
        angleDegre4 += 1
        """
        if(i > 90):
            i = 0
            A = 200
            B = 200
            C = 400
            D = 200

        A = (A - 300) * cos(i) - \
            (B - 300) * sin(i) + A
        B = (A - 300) * sin(i) + \
            (B - 300) * cos(i) + B

        C = (C - 300) * cos(i) - \
            (D - 300) * sin(i) + C
        D = (C - 300) * sin(i) + \
            (D - 300) * cos(i) + D
        """
        """
        A = A * cos(i) - B * sin(i) + 300
        B = B * cos(i) - A * sin(i) + 300
        C = C * cos(i) - D * sin(i) + 300
        D = D * cos(i) - C * sin(i) + 300
        """
        """
        A = A * cos(math.radians(i)) - B * sin(math.radians(math.radians(i))) + \
            (300 * (1 - cos(math.radians(i))) + 300 * sin(math.radians(i)))
        B = A * sin(math.radians(i)) + B * cos(math.radians(math.radians(i))) + \
            (300 * (1 - cos(math.radians(i)))
             + 300 * sin(math.radians(i)))
        C = A * cos(math.radians(i)) - B * sin(math.radians(math.radians(i))) + \
            (300 * (1 - cos(math.radians(i)))
             + 300 * sin(math.radians(i)))
        D = A * sin(math.radians(i)) + B * cos(math.radians(math.radians(i))) + \
            (300 * (1 - cos(math.radians(i)))
             + 300 * sin(math.radians(i)))
        """

        i += 1
        # cercle.draw(screen)
        # pygame.draw.lines(screen, RED, False, [[0, 80], [50, 90], [200, 80],
        # [220, 30]], 5)

        # pygame.draw.aaline(screen, GREEN, [0, 400],[640, 400], True) #
        # [width,height] to [width,height] une ligne

        # ligne multicolor
        """
        wblue = ligne(wblue)
        wblue2 = ligne(wblue2)
        wgreen = ligne(wgreen)
        wgreen2 = ligne(wgreen2)
        wred = ligne(wred)
        wred2 = ligne(wred2)
        """
        # pygame.draw.lines(screen, GREEN, False, [[426,400],[640,400]],6)
        """
        pygame.draw.lines(screen, BLUE, False, [[wblue,400],[wblue2,400]],6)
        pygame.draw.lines(screen, GREEN, False, [[wgreen,400],[wgreen2,400]],6)
        pygame.draw.lines(screen, RED, False, [[wred,400],[wred2,400]],6)
        pygame.draw.lines(screen, BLUE, False, [[wblue,400],[wblue2,400]],6)
        """

        # pygame.draw.lines(screen, RED, False, [[400-l,400],[400,400]],6)

        # pygame.draw.lines(screen, GREEN, False, [[600,300],[10,300]],6)
        # pygame.gfxdraw.line(screen, 600, 300, 10, 300, GREEN)
        # pygame.gfxdraw.hline(screen,50,200,300,RED)

        # center = [150, 200]
        # pygame.gfxdraw.aacircle(screen, center[0], center[1], 105, WHITE)
        # pygame.gfxdraw.aacircle(screen, center[0], center[1], 120, WHITE)
        # pygame.draw.arc(screen,RED, [30,70,240,245],0+i, pi/2+i, 20)

        # coord = 200
        # coord1 = 200
        # i += 0.02
        # screen.blit(carre, (0, 0))
        # pygame.transform.flip(carre, True, False)
        # Flip

        pygame.display.flip()  # met à jour la fenetre
        clock.tick(60)


# intro()
circle_loop()
pygame.display.quit()

quit()
