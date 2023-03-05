import pygame
import random
import math

pygame.init()

hitboxes = {
    "Red" : pygame.Rect(0, 0, 50, 50),
    "Blue" : pygame.Rect(0, 0, 50, 50)
}
hitboxes["Red"].topleft = hitboxes["Blue"].topright

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
    pygame.draw.rect(screen, "red", hitboxes["Red"])
    pygame.draw.rect(screen, "blue", hitboxes["Blue"])
    pygame.display.flip()
    break
pygame.time.wait(1000)

round = 0
point_red = 0
point_blue = 0
chosen = None

#User Choice
while (chosen is None):
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if hitboxes["Red"].collidepoint(event.pos):
                chosen = "Red"
            if hitboxes["Blue"].collidepoint(event.pos):
                chosen = "Blue"

#Main Loop
while round < 10:
    x_cor = random.randrange(0, 901)
    y_cor = random.randrange(0, 901)
    landing = (x_cor, y_cor)
    distance_from_center = math.hypot(450-x_cor, 450-y_cor)
    is_in_circle = distance_from_center
    if round % 2 == 0:
        if is_in_circle <= 900/2:
            pygame.draw.circle(screen, "red", landing, 10)
            pygame.display.flip()
            pygame.time.wait(1000)
            point_red = point_red + 1
        elif is_in_circle > 900/2:
            pygame.draw.circle(screen, "darkred", landing, 10)
            pygame.display.flip()
            pygame.time.wait(1000)
    elif not round % 2 == 0:
        if is_in_circle <= 900/2:
            pygame.draw.circle(screen, "blue", landing, 10)
            pygame.display.flip()
            pygame.time.wait(1000)
            point_blue = point_blue + 1
        elif is_in_circle > 900/2:
            pygame.draw.circle(screen, "darkblue", landing, 10)
            pygame.display.flip()
            pygame.time.wait(1000)
    round = round + 1

#Text Display
for score in range(1):
    font = pygame.font.Font(None, 48)
    if point_red == point_blue:
       text = font.render("It's a TIE!", True, "white")
       screen.blit(text, (390, 450))
       text1 = font.render(str(point_red), True, "red")
       screen.blit(text1, (424, 500))
       text2 = font.render(":", True, "white")
       screen.blit(text2, (444, 500))
       text3 = font.render(str(point_blue), True, "blue")
       screen.blit(text3, (464, 500))
       text4 = font.render("User's Guess is INCORRECT!", True, "white")
       screen.blit(text4, (230, 550))
       pygame.display.flip()
       pygame.time.wait(1000)
    elif point_red > point_blue:
        text = font.render("Player Red WINS!", True, "white")
        screen.blit(text, (300, 450))
        text1 = font.render(str(point_red), True, "red")
        screen.blit(text1, (424, 500))
        text2 = font.render(":", True, "white")
        screen.blit(text2, (444, 500))
        text3 = font.render(str(point_blue), True, "blue")
        screen.blit(text3, (464, 500))
        if chosen == "Red":
            text4 = font.render("User's Guess Red is CORRECT!", True, "white")
            screen.blit(text4, (230, 550))
        elif chosen == "Blue":
            text4 = font.render("User's Guess Blue is INCORRECT!", True, "white")
            screen.blit(text4, (230, 550))
        pygame.display.flip()
        pygame.time.wait(1000)
    elif point_red < point_blue:
        text = font.render("Player Blue WINS!", True, "white")
        screen.blit(text, (300, 450))
        text1 = font.render(str(point_red), True, "red")
        screen.blit(text1, (424, 500))
        text2 = font.render(":", True, "white")
        screen.blit(text2, (444, 500))
        text3 = font.render(str(point_blue), True, "blue")
        screen.blit(text3, (464, 500))
        if chosen == "Red":
            text4 = font.render("User's Guess Red is INCORRECT!", True, "white")
            screen.blit(text4, (230, 550))
        elif chosen == "Blue":
            text4 = font.render("User's Guess Blue is CORRECT!", True, "white")
            screen.blit(text4, (230, 550))
        pygame.display.flip()
        pygame.time.wait(1000)


