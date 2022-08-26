import pygame
pygame.init()
display = pygame.display.set_mode((1000, 800))
screen = pygame.Surface(display.get_size())
pygame.display.set_caption("Light")
clock = pygame.time.Clock()
done = False
dt = pygame.time.get_ticks()
rects = []
hold = False
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            hold = True
        elif event.type == pygame.MOUSEBUTTONUP:
            hold = False
    if hold:
        rects.append(pygame.Rect(pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1], 10, 10))
    screen.fill((170, 140, 0))
    for rect in rects:
        pygame.draw.rect(screen, (200, 200, 200), rect)
    display.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()