import pygame

pygame.init()

screen = pygame.display.set_mode()
screen.fill("white")
pygame.display.flip()
pygame.time.wait(5000)

screen_size = screen.get_size()
dimensions = [screen_size[0] / 2, screen_size[1] / 2, 250, 250]
dimensions = [[500, 500], 100]
pygame.draw.circle(screen, "red", dimensions)

dimensions = [[500, 450], 250]
pygame.draw.circle(screen, "blue", dimensions)

dimensions = [[500, 400], 250]
pygame.draw.circle(screen, "yellow", dimensions)

pygame.display.flip()
input()