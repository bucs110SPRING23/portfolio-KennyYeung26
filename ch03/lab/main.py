import pygame
import random
import math
#Part A:

pygame.init()

while 1:
    pygame.event.pump()
    screen = pygame.display.set_mode([900, 900])
    dimensions = screen.get_size()
    screen.fill("cyan2")
    starting_point = (dimensions[0] - 450, dimensions[1] - 450)
    pygame.draw.circle(screen, "cornflowerblue", starting_point, 450)
    pygame.draw.circle(screen, "black", starting_point, 450, 5)
    pygame.draw.line(screen, "black", (450,0) , (450,900), 5)
    pygame.draw.line(screen, "black", (0,450), (900,450), 5)
    pygame.display.flip()
    break
pygame.time.wait(1000)

#Part B:
for hit in range(0,10):
    x_cor = random.randrange(0, 901)
    y_cor = random.randrange(0, 901)
    landing = (x_cor, y_cor)
    distance_from_center = math.hypot(450-x_cor, 450-y_cor)
    is_in_circle = distance_from_center
    if is_in_circle <= 900/2:
        pygame.draw.circle(screen, "green", landing, 10)
        pygame.display.flip()
        pygame.time.wait(1000)
    elif is_in_circle >= 900/2:
        pygame.draw.circle(screen, "red", landing, 10)
        pygame.display.flip()
        pygame.time.wait(1000)
