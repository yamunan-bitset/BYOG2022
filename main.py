import pygame, random
pygame.init()
display = pygame.display.set_mode((1000, 800))
screen = pygame.Surface(display.get_size())
pygame.display.set_caption("Light")
clock = pygame.time.Clock()
done = False
dt = pygame.time.get_ticks()
circs = []
hold = False
pos = (random.randint(100, 900), random.randint(100, 700))
light = [(pos[0], pos[1])]
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            circs.append(pygame.mouse.get_pos())
    screen.fill((170, 140, 0))
    pygame.draw.circle(screen, (200, 100, 240), pos, 50)
    pygame.draw.circle(screen, (240, 170, 250), pos, 25)
    light.append((light[-1][0]+1, light[0][1]))
    i = 0
    for circ in circs:
        i += 1
        pygame.draw.circle(screen, (200, 200, 200), circ, 30)
        pygame.draw.circle(screen, (230, 230, 230), circ, 15)
        if i == 2:
            pygame.draw.line(screen, (210, 210, 210), circ, circ_, 3)
            i = 0
        else:
            circ_ = circ
    for lig in light:
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(lig[0], lig[1], 10, 10))
    display.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()