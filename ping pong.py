import pygame
import random


def getinput():
    global paddle1directiony, paddle2directiony, gamestate
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        paddle1directiony = -1
    elif keys[pygame.K_s]:
        paddle1directiony = 1
    else:
        paddle1directiony = 0

    if keys[pygame.K_UP]:
        paddle2directiony = -1
    elif keys[pygame.K_DOWN]:
        paddle2directiony = 1
    else:
        paddle2directiony = 0


def showscore():
    global score
    scoretext = font.render('Score: ' + str(score), True, 'White')
    scoretextrect = scoretext.get_rect(midtop=(400, 10))
    screen.blit(scoretext, scoretextrect)


pygame.init()

font = pygame.font.Font('freesansbold.ttf', 30)
score = 0

screen = pygame.display.set_mode((800, 500))
pygame.display.set_caption('ping pong')

ball = font.render('O', True, 'white')
ballrect = ball.get_rect(center=(400, 250))

paddle1 = pygame.Surface((10, 100))
paddle1.fill('white')
p1y = 10
paddle1rect = paddle1.get_rect(topleft=(10, p1y))

paddle2 = pygame.Surface((10, 100))
paddle2.fill('white')
p2y = 10
paddle2rect = paddle2.get_rect(topright=(790, p2y))

scoreline1 = pygame.Surface((1, 500))
scoreline1.fill('Black')
scoreline1rect = scoreline1.get_rect(topleft=(20, 0))
scoreline1state = True

scoreline2 = pygame.Surface((1, 500))
scoreline2.fill('Black')
scoreline2rect = scoreline2.get_rect(topleft=(780, 0))
scoreline2state = True

paddlespeed = 10
ballspeed = 5
difficulty = 1
frame = 0

if random.randint(1, 2):
    balldirectionx = 1
    ballgoingright = True
else:
    balldirectionx = -1
    ballgoingright = False
if random.randint(1, 2):
    balldirectiony = 1
else:
    balldirectiony = -1

gamestate = False

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    getinput()
    if gamestate:
        paddle1rect.y += paddle1directiony * paddlespeed
        paddle2rect.y += paddle2directiony * paddlespeed
        ballrect.x += balldirectionx * ballspeed * difficulty
        ballrect.y += balldirectiony * ballspeed * difficulty

        if paddle1rect.bottom >= 490:
            paddle1rect.bottom = 489
        elif paddle1rect.top <= 10:
            paddle1rect.top = 11

        if paddle2rect.bottom >= 490:
            paddle2rect.bottom = 489
        elif paddle2rect.top <= 10:
            paddle2rect.top = 11

        if ballrect.top <= 0:
            balldirectiony = 1
        elif ballrect.bottom >= 500:
            balldirectiony = -1
        if ballrect.colliderect(paddle1rect):
            balldirectionx = 1
        elif ballrect.colliderect(paddle2rect):
            balldirectionx = -1

        if ballrect.colliderect(scoreline1rect) and balldirectionx == 1 and scoreline1state:
            score += 1
            scoreline1state = False

        if ballrect.colliderect(scoreline2rect) and balldirectionx == -1 and scoreline2state:
            score += 1
            scoreline2state = False

        if ballrect.centerx >= 100:
            scoreline1state = True
        if ballrect.centerx <= 400:
            scoreline2state = True

        if ballrect.right <= 0 or ballrect.left >= 800:
            gamestate = False

        frame += 1
        if frame >= 100:
            frame -= 100
            difficulty += 1 / 15

        '''ballspeed1 = ballspeed*difficulty*100
        ballspeed1 = int(ballspeed1) / 100
        print ('ballspeed: ' + str(ballspeed1))'''

        screen.fill('black')
        screen.blit(ball, ballrect)
        screen.blit(paddle1, paddle1rect)
        screen.blit(paddle2, paddle2rect)
        showscore()

    else:
        screen.fill('black')
        showscore()
        text1 = font.render('Press Space to Start', True, 'White')
        text1rect = text1.get_rect(center=(400, 200))
        screen.blit(text1, text1rect)
        instructiontext = font.render('left paddle controls: w,s', True, 'White')
        instructiontext2 = font.render('right paddle controls: up key, down key', True, 'White')
        instructionrect = instructiontext.get_rect(center=(400, 250))
        instructionrect2 = instructiontext2.get_rect(center=(400, 300))
        screen.blit(instructiontext, instructionrect)
        screen.blit(instructiontext2, instructionrect2)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            gamestate = True
            score = 0
            ballrect.center = (400, 250)
            if random.randint(1, 2) == 2:
                balldirectionx = 1
                ballgoingright = True
            else:
                balldirectionx = -1
                ballgoingright = False
            if random.randint(1, 2) == 2:
                balldirectiony = 1
            else:
                balldirectiony = -1
            difficulty = 1

    pygame.display.update()
    pygame.time.Clock().tick(60)
