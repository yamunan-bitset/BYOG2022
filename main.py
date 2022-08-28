import pygame, random, math
pygame.init()
pygame.mixer.init()
display = pygame.display.set_mode((1000, 800))
screen = pygame.Surface(display.get_size())
pygame.display.set_caption("Light")
clock = pygame.time.Clock()
dt = pygame.time.get_ticks()
circs = []
circsf = []
hold = False
light_start = (random.randint(100, 900), random.randint(100, 700))
target_pos = (random.randint(100, 900), random.randint(100, 700))
light = light_start
lightf = lambda t: (t[0]+1, t[1])
done = False
collided = False
game_over_played = False
collision_points = [light_start]

channel1 = pygame.mixer.Channel(1)
hit = pygame.mixer.Sound("sfx/c.wav")
font = pygame.font.Font("freesansbold.ttf", 40)
source = pygame.image.load("gfx/source.png")
srect = source.get_rect()
srect.center = light_start
target = pygame.image.load("gfx/target.png")
trect = target.get_rect()
trect.center = target_pos

def text(msg, colour):
    text = font.render(msg, True, colour, (0, 0, 0))
    rect = text.get_rect()
    rect.centerx += 500 + random.randint(-3, 3)
    rect.centery += 400 + random.randint(-3, 3)
    screen.blit(text, rect)


def tmatrix(matrix, vector):
    return [matrix[0][0]*vector[0]+matrix[0][1]*vector[1], matrix[1][0]*vector[0]+matrix[1][1]*vector[1]]
def rmatrix(theta, vector, x):
    vec0 = tmatrix([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]], vector)
    vec1 = tmatrix([[math.cos(theta), -math.sin(theta)], [math.sin(theta), math.cos(theta)]], lightf(vector))
    m = (vec1[1] - vec0[1]) / (vec1[0] - vec0[0])
    c = vec0[1] - m * vec0[0]
    return m * x + c
pygame.mixer.Channel(0).play(pygame.mixer.Sound("sfx/a.wav"), maxtime=200)
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
    #screen.fill((170, 140, 0))
    screen.fill((0, 0, 0))
    screen.blit(source, srect)
    screen.blit(target, trect)
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
    
    pygame.draw.line(screen, (100, 0, 0), light, lightf(lightf(lightf(light))), 7)

    if light[0] > 1000 or light[0] < 0 or light[1] > 800 or light[1] < 0:
        if not game_over_played:
            pygame.mixer.Channel(2).play(pygame.mixer.Sound("sfx/e.wav"), maxtime=200)
            game_over_played = True
        text("Game Over!!", (100, 0, 0))
        dt = pygame.time.get_ticks()
        if dt - pygame.time.get_ticks() > 1000:
            break

    if math.isclose(light[0], target_pos[0], abs_tol = 40) and math.isclose(light[1], target_pos[1], abs_tol = 40):
        text("Congrats", (0, 0, 100))
        lightf = lambda t: t

    for y in range(len(circsf)):
        if math.isclose(circsf[y](light[0]), light[1], abs_tol = 5):
            collided = True
            dx = circs[y * 2][0] - light[0]
            dy = circs[y * 2][1] - light[1]
            d = math.sqrt(dx ** 2 + dy ** 2)
            theta = math.asin(dy/d)
            print("Collision!")
            print(f"{theta * 180 / math.pi=}")
            collision_points.append(light)
            lightf = lambda t: (t[0] - math.cos(math.pi+2*theta), t[1] - math.sin(math.pi+2*theta))
            channel1.play(hit, maxtime=200)

    display.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()