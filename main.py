import pygame, random, math
pygame.init()
display = pygame.display.set_mode((1000, 800))
screen = pygame.Surface(display.get_size())
pygame.display.set_caption("Light")
clock = pygame.time.Clock()
dt = pygame.time.get_ticks()
circs = []
circsf = []
hold = False
pos = (random.randint(100, 900), random.randint(100, 700))
light_start = (pos[0], pos[1])
light = light_start
done = False

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
    light = (light[0]+1, light[1])
    i = 0
    for circ1 in circs:
        i += 1
        pygame.draw.circle(screen, (200, 200, 200), circ1, 20)
        pygame.draw.circle(screen, (230, 230, 230), circ1, 10)
        if i % 2 == 0:
            pygame.draw.line(screen, (230, 230, 230), circ1, circ2, 5)
            m = ((circ1[1] - circ2[1])/(circ1[0] - circ2[0])) 
            c = circ1[1] - m * circ1[0]
            circsf.append(lambda x: m*x+c)
        else:
            circ2 = circ1
    pygame.draw.line(screen, (250, 250, 250), light_start, light, 5)
    for y in circsf:
        if math.isclose(y(light[0]), light[1], abs_tol = 5):
            print("Collision!")
    display.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()