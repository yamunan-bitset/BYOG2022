import pygame, random, math, numpy as np
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
lightf = lambda t: (t[0]+1, t[1])
done = False
collided = False

collision_points = [light_start]

def tmatrix(matrix, vector):
    return [matrix[0][0]*vector[0]+matrix[0][1]*vector[1], matrix[1][0]*vector[0]+matrix[1][1]*vector[1]]
def rmatrix(theta, vector, x):
    vec0 = tmatrix([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]], vector)
    vec1 = tmatrix([[np.cos(theta), -np.sin(theta)], [np.sin(theta), np.cos(theta)]], lightf(vector))
    m = (vec1[1] - vec0[1]) / (vec1[0] - vec0[0])
    c = vec0[1] - m * vec0[0]
    return m * x + c

while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            circs.append(pygame.mouse.get_pos())
            if len(circs) % 2 == 0:
                try:
                    m = (circs[-2][1] - circs[-1][1])/(circs[-2][0] - circs[-1][0])
                except ZeroDivisionError as d:
                    circs[-1] = (circs[-1][0] + 1, circs[-1][1])
                    m = (circs[-2][1] - circs[-1][1])/(circs[-2][0] - circs[-1][0])
                c = circs[-1][1] - m * circs[-1][0]
                circsf.append(lambda x: m*x+c)
    screen.fill((170, 140, 0))
    pygame.draw.circle(screen, (200, 100, 240), pos, 50)
    pygame.draw.circle(screen, (240, 170, 250), pos, 25)
    light = lightf(light)
    i = 0
    for circ1 in circs:
        i += 1
        pygame.draw.circle(screen, (200, 200, 200), circ1, 20)
        pygame.draw.circle(screen, (230, 230, 230), circ1, 10)
        if i % 2 == 0:
            pygame.draw.line(screen, (230, 230, 230), circ1, circ2, 5)
        else:
            circ2 = circ1

    if collided:
        pygame.draw.line(screen, (250, 250, 250), light_start, collision_points[0], 5)
        for i in range(len(collision_points) - 1):
            pygame.draw.line(screen, (250, 250, 250), collision_points[i], collision_points[i + 1], 5)
        pygame.draw.line(screen, (250, 250, 250), collision_points[-1], light, 5)
    else:
        pygame.draw.line(screen, (250, 250, 250), light_start, light, 5)

    for y in range(len(circsf)):
        if math.isclose(circsf[y](light[0]), light[1], abs_tol = 5):
            collided = True
            dx = circs[y][0] - light[0]
            dy = circs[y][1] - light[1]
            d = np.sqrt(dx ** 2 + dy ** 2)
            theta = np.arcsin(dy/d)
            print("Collision!")
            print(f"{theta * 180 / np.pi=}")
            collision_points.append(light)
            """y = lambda x: rmatrix((180+2*theta), light, x)
            lightf = lambda t: (t[0], y(t[0]))
            light = lightf(light)
            print(collision_points)"""
            lightf = lambda t: (t[0] - math.cos(np.pi+2*theta), t[1] - math.sin(np.pi+2*theta))
            break
    display.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()