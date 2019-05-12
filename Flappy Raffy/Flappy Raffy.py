
# Flappy Raffy Bird in Python PyGame #

# A GAME PROJECT PRESENTED TO: Univeristy of the Philippines High School in Iloilo
# Clone GitHub repository: git clone https://github.com/MapiyaAbalowa/Flappy-Bird-V2

# Created by:
# Cristobal, Yazmin Nievec
# Distajo, Kristel Jane
# Superio, KC S.

# Project started: 11 May 2019; 19:48, GMT + 8
# Project completed: 12 May 2019; 16:08, GMT + 8


import pygame
from pygame import *

import random
import os, sys

pygame.init()
SIZE = [1220, 730] 


def multimedia():

    backdrop = pygame.image.load("backdrop.png").convert()
    backdrop = pygame.transform.scale(backdrop, [1220, 730])

    b1 = pygame.transform.scale(pygame.image.load("b1.png").convert_alpha(), (50, 40))
    b2 = pygame.transform.scale(pygame.image.load("b2.png").convert_alpha(), (50, 40))

    b3 = pygame.transform.scale(pygame.image.load("b3.png").convert_alpha(), (50, 40))
    b4 = pygame.transform.scale(pygame.image.load("b4.png").convert_alpha(), (50, 40))


    zero = pygame.image.load("0.png").convert_alpha()
    one = pygame.image.load("1.png").convert_alpha()

    two = pygame.image.load("2.png").convert_alpha()
    three = pygame.image.load("3.png").convert_alpha()

    four = pygame.image.load("4.png").convert_alpha()
    five = pygame.image.load("5.png").convert_alpha()

    six = pygame.image.load("6.png").convert_alpha()
    seven = pygame.image.load("7.png").convert_alpha()

    eight = pygame.image.load("8.png").convert_alpha()
    nine = pygame.image.load("9.png").convert_alpha()

    point_up = pygame.image.load("pointup.png").convert_alpha()
    point_down = pygame.image.load("pointdown.png").convert_alpha()

    scoreboard = pygame.image.load("scoreboard.png").convert_alpha()
    start = pygame.image.load("start.png").convert_alpha()

    sprites = [b1, b2, b3, b4, point_up, point_down, scoreboard, start, backdrop]
    sounds = [pygame.mixer.Sound("die.wav"), pygame.mixer.Sound("hit.wav"), pygame.mixer.Sound("point.wav"), pygame.mixer.Sound("wing.wav")]
    scores = [zero, one, two, three, four, five, six, seven, eight, nine]


    mult = [sprites, sounds, scores]
    return mult

class Bird(pygame.sprite.Sprite):

    def __init__(bird):

        bird.x_pos = 50
        bird.y_pos = 350

        bird.fly = 0
        bird.fly_vel = 10

        bird.pull = 1
        bird.bumped = False

        bird.sprite = 0
        bird.bird_sprites = list(multimedia()[0][0:4])
        

    def motion(bird):

        if bird.bumped:
            
            bird.sprite = 3
            
            if bird.y_pos < SIZE[1] - 30:
                bird.y_pos += bird.pull

        elif bird.y_pos > 0:
            
            if bird.fly:

                bird.sprite = 1
                
                bird.fly_vel -= 2
                bird.y_pos -= bird.fly_vel

            else:

                bird.sprite = 2
                bird.pull += 2
                bird.y_pos += bird.pull

        else:
            
            bird.fly = 0
            bird.y_pos += 3

    def grounding(bird):
        
        if bird.y_pos >= SIZE[1] - 30:
            bird.bumped = True

    def rec_pos(bird):
        
        sprite_rec = bird.bird_sprites[bird.sprite].get_rect()
        sprite_rec[0] = bird.x_pos

        sprite_rec[1] = bird.y_pos
        return sprite_rec


class Towers(pygame.sprite.Sprite):

    def __init__(tower, place):
        
        tower.place = place
        tower.sprite = tower.sprite_img()

    def tower_pos(tower):
       
        return tower.sprite.get_rect()

    def sprite_img(tower):

        up = multimedia()[0][5]
        down = multimedia()[0][4]

        if tower.place:  
            return up

        else:  
            return down


class Choices(object):
    
    def __init__(ch):

        ch.scoreboard =  multimedia()[0][6]
        ch.start_button = multimedia()[0][7]

        ch.start_rpos = ch.start_button.get_rect()
        ch.board_rpos = ch.scoreboard.get_rect()

        ch.xy_pos()
        ch.points = 0

    def xy_pos(ch):

        ch.start_rpos.center = (610, 420)
        ch.board_rpos.center = (610, 300)

    def add_score(ch):
       
        ch.points += 1
        multimedia()[1][2].play()


class Main_Platform(object):

    def __init__(game):
        
        game.surface = pygame.display.set_mode(SIZE)
        pygame.display.set_caption("Flappy Bird")
        
        game.backdrop = multimedia()[0][8]
        
        game.screen_offset = 0
        game.tower_xpos = 1100

        game.screen_offset_a = 4
        game.screen_offset_b = 6

        game.screen_offset_c = 9
        game.screen_offset_d = 13

        game.tower_xposa = 900
        game.tower_xposb = 700

        game.tower_xposc = 500
        game.tower_xposd = 300

        game.TowerUp = Towers(1)  
        game.TowerDown = Towers(0)

        game.TowerUpA = Towers(1)  
        game.TowerDownA = Towers(0)

        game.TowerUpB = Towers(1)  
        game.TowerDownB = Towers(0)

        game.TowerUpC = Towers(1)  
        game.TowerDownC = Towers(0)

        game.TowerUpD = Towers(1)  
        game.TowerDownD = Towers(0)

        game.gaps = 120
        game.Bird = Bird()  

        game.Scoring = Choices()
        game.track = False  

    def tower_motion(game):
        
        if game.tower_xpos < -100:

            game.screen_offset = random.randrange(-130, 130)
            game.track = False

            game.tower_xpos = 1100

        game.tower_xpos -= 5

    def tower_motion_A(game):
        
        if game.tower_xposa < -100:

            game.screen_offset_a = random.randrange(-130, 130)
            game.track = False

            game.tower_xposa = 1100

        game.tower_xposa -= 5

    def tower_motion_B(game):
        
        if game.tower_xposb < -100:

            game.screen_offset_b = random.randrange(-130, 130)
            game.track = False

            game.tower_xposb = 1100

        game.tower_xposb -= 5

    def tower_motion_C(game):
        
        if game.tower_xposc < -100:

            game.screen_offset_c = random.randrange(-130, 130)
            game.track = False

            game.tower_xposc = 1100

        game.tower_xposc -= 5

    def tower_motion_D(game):
        
        if game.tower_xposd < -100:

            game.screen_offset_d = random.randrange(-130, 130)
            game.track = False

            game.tower_xposd = 1100

        game.tower_xposd -= 5
        
        
    def tower_rec(game, tower):
        
        r = tower.sprite.get_rect()
        r[0] = game.tower_xpos

        if tower.place:
            
            r[1] = 0 - game.gaps - game.screen_offset
        else:
            
            r[1] = 400 + game.gaps - game.screen_offset

        return r

    def tower_rec_A(game, tower):
        
        r = tower.sprite.get_rect()
        r[0] = game.tower_xposa 

        if tower.place:
            
            r[1] = 0 - game.gaps - game.screen_offset_a
        else:
            
            r[1] = 400 + game.gaps - game.screen_offset_a

        return r

    def tower_rec_B(game, tower):
        
        r = tower.sprite.get_rect()
        r[0] = game.tower_xposb

        if tower.place:
            
            r[1] = 0 - game.gaps - game.screen_offset_b
        else:
            
            r[1] = 400 + game.gaps - game.screen_offset_b

        return r

    def tower_rec_C(game, tower):
        
        r = tower.sprite.get_rect()
        r[0] = game.tower_xposc

        if tower.place:
            
            r[1] = 0 - game.gaps - game.screen_offset_c
        else:
            
            r[1] = 400 + game.gaps - game.screen_offset_c

        return r

    def tower_rec_D(game, tower):
        
        r = tower.sprite.get_rect()
        r[0] = game.tower_xposd

        if tower.place:
            
            r[1] = 0 - game.gaps - game.screen_offset_d
        else:
            
            r[1] = 400 + game.gaps - game.screen_offset_d

        return r

    def bumping(game):

       up_r = game.tower_rec(game.TowerUp)
       down_r = game.tower_rec(game.TowerDown)

       up_ra = game.tower_rec_A(game.TowerUpA)
       down_ra = game.tower_rec_A(game.TowerDownA)

       up_rb = game.tower_rec_B(game.TowerUpB)
       down_rb = game.tower_rec_B(game.TowerDownB)

       up_rc = game.tower_rec_C(game.TowerUpC)
       down_rc = game.tower_rec_C(game.TowerDownC)

       up_rd = game.tower_rec_D(game.TowerUpD)
       down_rd = game.tower_rec_D(game.TowerDownD)

       if up_r.colliderect(game.Bird.rec_pos()) or down_r.colliderect(game.Bird.rec_pos()):

           game.Bird.bumped = True
           multimedia()[1][1].play()
           multimedia()[1][0].play()

       elif not game.track and up_r.right < game.Bird.x_pos:

           game.Scoring.add_score()
           game.track = True


       if up_ra.colliderect(game.Bird.rec_pos()) or down_ra.colliderect(game.Bird.rec_pos()):

           game.Bird.bumped = True
           multimedia()[1][1].play()
           multimedia()[1][0].play()

       elif not game.track and up_ra.right < game.Bird.x_pos:

           game.Scoring.add_score()
           game.track = True

       if up_rb.colliderect(game.Bird.rec_pos()) or down_rb.colliderect(game.Bird.rec_pos()):

           game.Bird.bumped = True
           multimedia()[1][1].play()
           multimedia()[1][0].play()

       elif not game.track and up_rb.right < game.Bird.x_pos:

           game.Scoring.add_score()
           game.track = True

       if up_rc.colliderect(game.Bird.rec_pos()) or down_rc.colliderect(game.Bird.rec_pos()):

           game.Bird.bumped = True
           multimedia()[1][1].play()
           multimedia()[1][0].play()

       elif not game.track and up_rc.right < game.Bird.x_pos:

           game.Scoring.add_score()
           game.track = True

       if up_rd.colliderect(game.Bird.rec_pos()) or down_rd.colliderect(game.Bird.rec_pos()):

           game.Bird.bumped = True
           multimedia()[1][1].play()
           multimedia()[1][0].play()

       elif not game.track and up_rd.right < game.Bird.x_pos:

           game.Scoring.add_score()
           game.track = True
    

    def repeat(game):

        game.Scoring.points = 0
        game.Bird = Bird()

        game.TowerUp = Towers(1)
        game.TowerDown = Towers(0)

        game.TowerUpA = Towers(1)  
        game.TowerDownA = Towers(0)

        game.TowerUpB = Towers(1)  
        game.TowerDownB = Towers(0)

        game.TowerUpC = Towers(1)  
        game.TowerDownC = Towers(0)

        game.TowerUpD = Towers(1)  
        game.TowerDownD = Towers(0)

        game.tower_xpos = 1100

        game.tower_xposa = 900
        game.tower_xposb = 700

        game.tower_xposc = 500
        game.tower_xposd = 300
        
        game.Bird.acc = 9.8


    def reveal(game):
        
        game.points = game.Scoring.points
        game.img_pt = list(multimedia()[2])

        if game.points < 10:

            game.tens = game.img_pt[0]
            game.ones = game.img_pt[game.points]

            game.surface.blit(game.tens, (570, 50))
            game.surface.blit(game.ones, (610, 50))

        elif game.points >= 10:

            game.ln = []
            game.score = str(game.points)

            for digit in game.score:
                game.ln.append(digit)

            game.tens = game.img_pt[int(game.ln[0])]
            game.ones = game.img_pt[int(game.ln[1])]

            game.surface.blit(game.tens, (560, 50))
            game.surface.blit(game.ones, (610, 50))                

    def done(game):

        start_rpos = game.Scoring.start_rpos
        board_rpos = game.Scoring.board_rpos

        game.surface.blit(game.Scoring.scoreboard, board_rpos)
        game.surface.blit(game.Scoring.start_button, start_rpos)

        game.points = game.Scoring.points
        game.img_pt = list(multimedia()[2])

        if game.points < 10:

            game.tens = game.img_pt[0]
            game.ones = game.img_pt[game.points]

            game.surface.blit(game.tens, (580, 300))
            game.surface.blit(game.ones, (620, 300))

        elif game.points >= 10:

            game.ln = []
            game.score = str(game.points)

            for digit in game.score:
                game.ln.append(digit)

            game.tens = game.img_pt[int(game.ln[0])]
            game.ones = game.img_pt[int(game.ln[1])]

            game.surface.blit(game.tens, (580, 300))
            game.surface.blit(game.ones, (620, 300))
            

    def game_loop(game):

        clock = pygame.time.Clock()
       
        while True:

            clock.tick(60)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:

                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    
                    if event.key == pygame.K_SPACE or event.key == K_UP:

                        multimedia()[1][3].play()

                        game.Bird.sprite = 1
                        game.Bird.sprite = 0

                        game.Bird.fly = 17
                        game.Bird.pull = 9.8
                        game.Bird.fly_vel = 10

                if event.type == pygame.KEYUP:

                    game.Bird.sprite = 2

                if event.type == pygame.MOUSEBUTTONDOWN:
                    
                    if game.Bird.bumped and game.Scoring.start_rpos.collidepoint(event.pos):

                        game.Bird.bumped = False
                        game.repeat()

            game.surface.blit(game.backdrop, (0, 0))

            game.surface.blit(game.TowerUp.sprite, (game.tower_xpos, 0 - game.gaps - game.screen_offset))
            game.surface.blit(game.TowerDown.sprite, (game.tower_xpos, 360 + game.gaps - game.screen_offset))

            game.surface.blit(game.TowerUpA.sprite, (game.tower_xposa, 0 - game.gaps - game.screen_offset_a))
            game.surface.blit(game.TowerDownA.sprite, (game.tower_xposa, 360 + game.gaps - game.screen_offset_a))

            game.surface.blit(game.TowerUpB.sprite, (game.tower_xposb, 0 - game.gaps - game.screen_offset_b))
            game.surface.blit(game.TowerDownB.sprite, (game.tower_xposb, 360 + game.gaps - game.screen_offset_b))

            game.surface.blit(game.TowerUpC.sprite, (game.tower_xposc, 0 - game.gaps - game.screen_offset_c))
            game.surface.blit(game.TowerDownC.sprite, (game.tower_xposc, 360 + game.gaps - game.screen_offset_c))

            game.surface.blit(game.TowerUpD.sprite, (game.tower_xposd, 0 - game.gaps - game.screen_offset_d))
            game.surface.blit(game.TowerDownD.sprite, (game.tower_xposd, 360 + game.gaps - game.screen_offset_d))

            game.surface.blit(game.Bird.bird_sprites[game.Bird.sprite], (game.Bird.x_pos, game.Bird.y_pos))

            game.tower_motion()

            game.tower_motion_A()
            game.tower_motion_B()

            game.tower_motion_C()
            game.tower_motion_D()

            game.Bird.motion() 
            game.Bird.grounding()
            
            if not game.Bird.bumped:
                
                game.bumping()
                game.reveal()

            else:
                
                game.done()

            pygame.display.flip()


os.chdir(os.path.dirname(__file__))
if __name__ == "__main__":

    main = Main_Platform()
    main.game_loop()

    
