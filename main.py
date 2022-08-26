import pygame
pygame.init()
display = pygame.display.set_mode((1000, 800))
screen = pygame.Surface(display.get_size())
pygame.display.set_caption("")
clock = pygame.time.Clock()
done = False
dt = pygame.time.get_ticks()
while not done:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            break
    screen.fill((170, 140, 0))
    display.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()