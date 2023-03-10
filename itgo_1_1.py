import pygame
from pygame.constants import QUIT

White = (255, 255, 255)
Black = (0, 0, 0)

pygame.init()

screen = width, height = 800, 600

main_surface = pygame.display.set_mode(screen)

ball = pygame.Surface((20, 20))
ball.fill(White)
ball_rect = ball.get_rect()
ball_speed = [1, 1]


is_working = True

while(is_working):
    for event in pygame.event.get():
        if event.type == QUIT: 
            is_working= False

    ball_rect = ball_rect.move(ball_speed)

    if ball_rect.bottom >= height or ball_rect.top <= 0: 
        ball_speed[1] = -ball_speed[1]
        ball.fill(rand_color)
    
    main_surface.fill(Black)
    main_surface.blit(ball, ball_rect)
    pygame.display.flip()