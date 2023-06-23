import sys

import pygame, time, random

winwidth = 1600
winheight = 1000
playerx = 300
playery = 400
speed = 10
laserx = 800
lasery = -100
laserINDCx = 800
laserINDCy = -100
vertlaserx = -100
vertlasery = 500
vertlaserINDCx = -100
vertlaserINDCy = 500
vertlaser2x = -100
vertlaser2y = 500
vertlaserINDC2x = 400
vertlaserINDC2y = 500
difficulty = 1.5
deathcount = 0
laserdecide = 0
laseractivate = 0
playing = True
gameover = False
gameoverforceend = False

class Player(pygame.sprite.Sprite):

    def __init__(self, speed, color):
        super().__init__()
        self.image = pygame.Surface((50, 80), pygame.SRCALPHA)
        pygame.draw.rect(self.image, 'purple', self.image.get_rect())
        self.rect = self.image.get_rect()

        self.pos = pygame.Vector2(playerx, playery)
        self.target = pygame.Vector2(playerx, playery)
        self.speed = speed

    def update(self):
        move = self.target - self.pos
        move_length = move.length()

        if move_length != 0:
            move.normalize_ip()
            move = move * min(move_length, self.speed)
            self.pos += move

        self.rect.center = self.pos

class Laser(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((winwidth, 100), pygame.SRCALPHA)
        self.image.fill(pygame.Color(255, 0, 0, 255))
        self.rect = self.image.get_rect(center=(laserx, lasery))

class LaserINDC(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((winwidth, 100), pygame.SRCALPHA)
        self.image.fill(pygame.Color(255, 0, 0, 50))
        self.rect = self.image.get_rect(center=(laserINDCx, laserINDCy))

class vertLaser(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, winheight), pygame.SRCALPHA)
        self.image.fill(pygame.Color(255, 0, 0, 255))
        self.rect = self.image.get_rect(center=(vertlaserx, vertlasery))

class vertLaserINDC(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, winheight), pygame.SRCALPHA)
        self.image.fill(pygame.Color(255, 0, 0, 50))
        self.rect = self.image.get_rect(center=(vertlaserINDCx, vertlaserINDCy))

class vertLaser2(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, winheight), pygame.SRCALPHA)
        self.image.fill(pygame.Color(255, 0, 0, 255))
        self.rect = self.image.get_rect(center=(vertlaser2x, vertlaser2y))

class vertLaserINDC2(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, winheight), pygame.SRCALPHA)
        self.image.fill(pygame.Color(255, 0, 0, 50))
        self.rect = self.image.get_rect(center=(vertlaserINDC2x, vertlaserINDC2y))

class gameOver(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((winwidth, winheight), pygame.SRCALPHA)
        self.image.fill(pygame.Color(135, 206, 235, 255))
        self.rect = self.image.get_rect(center=(winwidth/2, winheight/2))

def main():

    global speed
    global lasery
    global laserINDCy
    global vertlaserx
    global vertlaserINDCx
    global vertlaser2x
    global vertlaserINDC2x
    global difficulty
    global deathcount
    global laserdecide
    global laseractivate
    global playing
    global gameover
    global gameoverforceend

    pygame.init()

    screen = pygame.display.set_mode((winwidth, winheight), pygame.SRCALPHA)
    pygame.display.set_caption("League Of Legends")

    clock = pygame.time.Clock()
    start_time = time.time()

    start_time2 = time.time()

    start_time3 = time.time()

    start_time4 = time.time()

    start_time5 = time.time()

    start_time6 = time.time()

    player = pygame.sprite.Group(Player(speed, pygame.Color(255, 0, 0, 255)))

    laser = Laser()
    laser_group = pygame.sprite.Group()
    laser_group.add(laser)

    laserINDC = LaserINDC()
    laserINDC_group = pygame.sprite.Group()
    laserINDC_group.add(laserINDC)

    vertlaser = vertLaser()
    vertlaser_group = pygame.sprite.Group()
    vertlaser_group.add(vertlaser)

    vertlaserINDC = vertLaserINDC()
    vertlaserINDC_group = pygame.sprite.Group()
    vertlaserINDC_group.add(vertlaserINDC)

    vertlaser2 = vertLaser()
    vertlaser2_group = pygame.sprite.Group()
    vertlaser2_group.add(vertlaser2)

    vertlaserINDC2 = vertLaserINDC()
    vertlaserINDC2_group = pygame.sprite.Group()
    vertlaserINDC2_group.add(vertlaserINDC2)

    gameover = gameOver()
    gameover_group = pygame.sprite.Group()
    gameover_group.add(gameover)

    running = True
    while running:

        if playing:

            time_alive = time.time()
            time_difference = time_alive - start_time

            time_alive2 = time.time()
            time_difference2 = time_alive2 - start_time2

            time_alive5 = time.time()
            time_difference5 = time_alive5 - start_time5

            time_alive6 = time.time()
            time_difference6 = time_alive6 - start_time6

            font = pygame.font.SysFont("Times New Roman", 60, False, False)
            font_image = font.render(str(round(time_difference5, 2)), True, (255, 255, 255))
            gameover_text = font.render('Game Over', True, (255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    for movement in player.sprites():
                        movement.target = pygame.mouse.get_pos()

            if pygame.sprite.groupcollide(player, laser_group, True, True):
                player = pygame.sprite.Group(Player(6, pygame.Color(160, 32, 240, 255)))
                laser = Laser()
                laser_group = pygame.sprite.Group()
                laser_group.add(laser)
                start_time = time_alive
                start_time2 = time_alive2
                playing = False

            if pygame.sprite.groupcollide(player, vertlaser_group, True, True):
                player = pygame.sprite.Group(Player(6, pygame.Color(160, 32, 240, 255)))
                vertlaser = vertLaser()
                vertlaser_group = pygame.sprite.Group()
                vertlaser_group.add(vertlaser)
                start_time = time_alive
                start_time2 = time_alive2
                playing = False

            if pygame.sprite.groupcollide(player, vertlaser2_group, True, True):
                player = pygame.sprite.Group(Player(6, pygame.Color(160, 32, 240, 255)))
                vertlaser2 = vertLaser()
                vertlaser2_group = pygame.sprite.Group()
                vertlaser2_group.add(vertlaser2)
                start_time = time_alive
                start_time2 = time_alive2
                playing = False

            if time_difference >= 1:
                laserINDCy = random.randint(100, 900)
                laserINDC = LaserINDC()
                laserINDC_group = pygame.sprite.Group()
                laserINDC_group.add(laserINDC)
                start_time = time_alive

            if time_difference2 >= difficulty:
                lasery = laserINDCy
                laser = Laser()
                laser_group = pygame.sprite.Group()
                laser_group.add(laser)
                start_time = time_alive
                start_time2 = time_alive2

            if time_difference >= 1:
                vertlaserINDCx = random.randint(100, 1500)
                vertlaserINDC = vertLaserINDC()
                vertlaserINDC_group = pygame.sprite.Group()
                vertlaserINDC_group.add(vertlaserINDC)
                start_time = time_alive

            if time_difference2 >= difficulty:
                vertlaserx = vertlaserINDCx
                vertlaser = vertLaser()
                vertlaser_group = pygame.sprite.Group()
                vertlaser_group.add(vertlaser)
                start_time = time_alive
                start_time2 = time_alive2

            if time_difference >= 1:
                vertlaserINDC2x = random.randint(100, 1500)
                vertlaserINDC2 = vertLaserINDC2()
                vertlaserINDC2_group = pygame.sprite.Group()
                vertlaserINDC2_group.add(vertlaserINDC2)
                start_time = time_alive

            if time_difference2 >= difficulty:
                vertlaser2x = vertlaserINDC2x
                vertlaser2 = vertLaser2()
                vertlaser2_group = pygame.sprite.Group()
                vertlaser2_group.add(vertlaser2)
                start_time = time_alive
                start_time2 = time_alive2

            player.update()
            screen.fill('dark green')
            player.draw(screen)
            laser_group.draw(screen)
            laserINDC_group.draw(screen)
            vertlaser_group.draw(screen)
            vertlaserINDC_group.draw(screen)
            vertlaser2_group.draw(screen)
            vertlaserINDC2_group.draw(screen)
            screen.blit(font_image, [winwidth - 175, 25])

        else:
            gameover_group.draw(screen)
            screen.blit(gameover_text, [winwidth/2 - 120, winheight/2 - 60])
            gameoverforceend = True



        pygame.display.flip()
        clock.tick(60)


    pygame.quit()


if __name__ == "__main__":
    main()