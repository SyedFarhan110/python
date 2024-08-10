import pygame,sys,random

class Mygame():
    def main():
        # intial Speed
        Xspeed = 10
        yspeed = 10
        paddleSpeed = 30
        points = 0
        bgcolor = 0, 0, 0
        size = width, height = 500, 500

        #initializing pygame
        pygame.init()
        screen = pygame.display.set_mode(size)
        paddle = pygame.image.load('bat.jpg')
        paddleret = paddle.get_rect()

        ball = pygame.image.load('ball.jpg')
        ballrect = pygame.get_rect()

        bg = pygame.image.load('bggame.jpg')
        