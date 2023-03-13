import pygame

#Part A:

def threenp1(n):
    while not n == 1:
        count = 0
        while n > 1.0:
            if n % 2 == 0:
                n = int(n / 2)
            else:
                n = int(3 * n + 1)
            count = count + 1
        return count

def threenp1range(upper_limit):
    objs_in_sequence = {}
    for i in range(2, upper_limit + 1):
        count = threenp1(i)
        objs_in_sequence[i] = count
    return objs_in_sequence

def main():
    print(threenp1range(10))

main()

def graph_coordinates(threenplus1_iters_dict):
    pygame.init()
    while 1:
        pygame.event.pump()
        screen = pygame.display.set_mode()
        dimensions = screen.get_size()
        pygame.draw.lines(screen, "blue", False, list(threenplus1_iters_dict.items()))
        new_display = pygame.transform.flip(screen, False, True)
        width, height = new_display.get_size()
        new_display = pygame.transform.scale(new_display, (width * 5, height * 5))
        screen.blit(new_display, (0, 0))
        pygame.display.flip()
        break
    pygame.time.wait(6000)
graph_coordinates(threenp1range(10))