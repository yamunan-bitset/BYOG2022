import pygame, random, numpy as np
pygame.init()
display = pygame.display.set_mode((1000, 800))
screen = pygame.Surface(display.get_size())
pygame.display.set_caption("Light")
clock = pygame.time.Clock()
dt = pygame.time.get_ticks()
circs = []
hold = False
pos = (random.randint(100, 900), random.randint(100, 700))
light = [(pos[0], pos[1])]
done = False

lin_fs = []
def lin_f(circ1, circ2):
    m = ((circ1[1] - circ2[1])/(circ1[0] - circ2[0])) 
    c = circ1[1] - m * circ1[0]
    x = list(range(abs(circ1[1] - circ2[1])))
    return list(m * np.array(x) + c)

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
    for circ1 in circs:
        i += 1
        pygame.draw.circle(screen, (200, 200, 200), circ1, 20)
        pygame.draw.circle(screen, (230, 230, 230), circ1, 10)
        if i % 2 == 0:
            pygame.draw.line(screen, (230, 230, 230), circ1, circ2, 5)
            lin_fs.append(lin_f(circ1, circ2))
            print(lin_f(circ1, circ2))
        else:
            circ2 = circ1
    for lig in light:
        pygame.draw.rect(screen, (240, 170, 250), pygame.Rect(lig[0], lig[1], 10, 10))
        for f in lin_fs:
            for i in f:
                if lig[0] == i:
                    print("Collision?")
    display.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()