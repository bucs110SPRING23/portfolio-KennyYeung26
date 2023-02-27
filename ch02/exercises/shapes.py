import pygame

pygame.init()

screen = pygame.display.set_mode()
dimensions = screen.get_size()
starting_point = (dimensions[0] // 2, dimensions[1] // 2 + 120)

pygame.draw.circle(screen, "blue", starting_point, 200)

starting_point = (dimensions[0] // 2, dimensions[1] // 2 - 200)
pygame.draw.circle(screen, "yellow", starting_point, 120)

starting_point = (dimensions[0] // 2, dimensions[1] // 2 - 390)
pygame.draw.circle(screen, "red", starting_point, 70)

pygame.display.flip()
pygame.time.wait(1000)
input()
