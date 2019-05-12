

# Flappy Miles Game


import pygame, livewires
import os, sys
import math, random
    

pygame.init()
size = [1220, 720]  
pygame.mouse.set_visible(1)


def multimedia():

    backdrop = pygame.image.load("backdrop.png").convert()
    backdrop = pygame.transform.scale(backdrop, [1220, 720])

    b1 = pygame.image.load("b1.png").convert_alpha()
    b2 = pygame.image.load("b2.png").convert_alpha()

    b3 = pygame.image.load("b3.png").convert_alpha()
    b4 = pygame.image.load("b4.png").convert_alpha()

    point_up = pygame.image.load("pointup.png").convert_alpha()
    point_down = pygame.image.load("pointdown.png").convert_alpha()

    scoreboard = pygame.image.load("scoreboard.png").convert_alpha()
    start = pygame.image.load("start.png").convert_alpha()

    sprites = [b1, b2, b3, point_up, point_down, scoreboard, start, backdrop]
    sounds = [pygame.mixer.Sound("audio/die.wav"), pygame.mixer.Sound("audio/hit.wav"), pygame.mixer.Sound("audio/point.wav"), pygame.mixer.Sound("audio/wing.wav")]

    mult = [sprites, sounds]
    return mult
    
class Bird_Sprite:

    def __init__(bird):

        bird.x_pos = 60
        bird.y_pos = 260

        bird.fly = 0
        bird.y_vel = 12
        
        bird.acc = 3
        bird.bumped = False

        bird.image = 0   
        bird.sprite_list = list(multimedia()[0][0:4])

    def motion(bird):

        if bird.bumped:
            bird.image = 3

            if bird.y_pos < size[1] - 48:
                bird.y_pos += bird.acc

        elif bird.y_pos > 0:

            if bird.fly:

                bird.image = 0
                bird.y_vel -= 1
                bird.y_pos -= bird.y_vel

            else:

                bird.acc += 0.2
                bird.y_pos += bird.acc

        else:

            bird.fly = 0
            bird.y_pos += 3

    def grounding(bird):

        if bird.y_pos >= size[1] - 48:
            bird.bumped = True

    def rec_pos(bird):

        rec_pos = bird.sprite_list[bird.image].get_rect()
        rec_pos[0] = bird.x_pos
        rec_pos[1] = bird.y_pos

        return rec_pos

class Tower_Sprite:

    def __init__(tower, place):

        tower.place = place
        tower.sprite = tower.sprite()

    def rec_pos(tower):
        return tower.sprite.get_rect()

    def sprite(tower):

        up = multimedia()[0][3]
        down = multimedia()[0][4]

        if tower.place:
            return up

        else:
            return down
        
class Choices(object):

    def __init__(ch):

        ch.scoreboard = multimedia()[0][5]
        ch.start_button = multimedia()[0][6]

        ch.start_rpos = ch.start_button.get_rect()
        ch.sc_rpos = ch.scoreboard.get_rect()

        ch.xy_pos()
        ch.points = 0


    def xy_pos(ch):
        ch.start_rpos.center = (610, 360)
        ch.sc_rpos.center = (610, 250)

    def scoring(ch):
        ch.points += 1


class Main_Platform:

    def __init__(game):
        
        game.surface = pygame.display.set_mode(size)
        pygame.display.set_caption("FLAPPY MILES")

        game.backdrop = multimedia()[0][7]
        game.tower_xpos = 699

        game.screen_offset = 0

        game.TowerUp = Tower_Sprite(1)
        game.TowerDown = Tower_Sprite(0)

        game.gaps = 150

        game.Bird = Bird_Sprite()
        game.Scoring = Choices()

        game.track = False

    def tower_motion(game):

        if game.tower_xpos < -106:

            game.screen_offset = random.randrange(-120, 120)
            game.track = False
            game.tower_xpos = 699

        game.tower_xpos -= 5

    def game_loop(game):

        fps = pygame.time.Clock()

        while True:

            fps.tick(60)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_SPACE:

                        game.Bird.fly = 20
                        game.Bird.acc = 2
                        game.Bird.y_vel = 10

                if  event.type == pygame.MOUSEBUTTONDOWN:

                    if game.Bird.bumped and game.Scoring.start_rpos.collidepoint(event.pos):

                        game.Bird.bumped = False
                        game.repeat()

            game.surface.blit(game.backdrop, (0, 0))
            game.surface.blit(game.TowerUp.sprite, (game.tower_xpos, 0 - game.gaps - game.screen_offset))

            game.surface.blit(game.TowerDown.sprite, (game.tower_xpos, 360 + game.gaps - game.screen_offset))
            game.surface.blit(game.Bird.sprite_list[game.Bird.image], (game.Bird.x_pos, game.Bird.y_pos))

            game.tower_motion()
            game.Bird.motion()
            game.Bird.grounding()

            if not game.Bird.bumped:

                game.bumping()
                game.reveal()

            else:

                game.done()

            pygame.display.flip()
        

    def tower_rec(game, tower):

        r = tower.sprite.get_rect()
        r[0] = game.tower_xpos

        if tower.place:

            r[1] = 0 - game.gaps - game.screen_offset

        else:

            r[1] = 360 + game.gaps + game.screen_offset

        return r

    def bumping(game):

        up_r = game.tower_rec(game.TowerUp)
        down_r = game.tower_rec(game.TowerDown)

        if up_r.colliderect(game.Bird.rec_pos()) or down_r.colliderect(game.Bird.rec_pos()):

            game.Bird.bumped = True

        elif not game.track and up_r.right < game.Bird.x_pos:

            game.Scoring.scoring()
            game.track = True


    def repeat(game):

        game.Scoring.points = 0
        game.bird = Bird_Sprite()

        game.TowerUp = Tower_Sprite(1)
        game.TowerDown = Tower_Sprite(0)

        game.tower_xpos = 699
        game.Bird.acc = 2

    def reveal(game):

        score_font = pygame.font.SysFont('arialrounded', 50).render("{}".format(game.Scoring.scoring), True, (255, 80, 80))

        font_rect = score_font.get_rect()
        font_rect.center = (200, 50)
        game.surface.blit(score_font, font_rect)


    def done(game):


        score_font = pygame.font.SysFont('arialrounded', 50).render("{}".format(game.Scoring.scoring), True, (255, 80, 80))
        font_rect = score_font.get_rect()
        score_rect = game.Scoring.sc_rpos

        play_rect = game.Scoring.start_rpos  # play button rectangle
        font_rect.center = (200, 230)
        game.surface.blit(game.Scoring.start_button, game.Scoring.start_rpos)  # show play button
        game.surface.blit(game.Scoring.scoreboard, game.Scoring.sc_rpos)  # show score board image
        game.surface.blit(score_font, font_rect)


    

os.chdir(os.path.dirname(__file__))
if __name__ == "__main__":
    loop = Main_Platform()
    loop.game_loop()


            
 

        
        
        
    
                

            
        
