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

def graph_coordinates(threenplus1_iters_dict):
    pygame.init()
    while 1:
        pygame.event.pump()
        display = pygame.display.set_mode()
        pygame.draw.lines(display, "blue", False, list(threenplus1_iters_dict.items()))
        dictionary = list(threenplus1_iters_dict.items())
        max_so_far = 0
        for i in range(len(dictionary)):
            if (dictionary[i][1] > max_so_far):
                max_so_far = dictionary[i][1]
        new_display = pygame.transform.flip(display, False, True)
        width, height = new_display.get_size()
        new_display = pygame.transform.scale(new_display, (width * 5, height * 5))
        display.blit(new_display, (0, 0))
        font = pygame.font.Font(None, 48)
        msg = font.render(("Max so far is: "+ str(max_so_far)), False, "Blue")
        display.blit(msg, (1150,10))
        pygame.display.flip()
        break
    pygame.time.wait(6000)

def main():
    print(threenp1range(20))
    graph_coordinates(threenp1range(20))

main()