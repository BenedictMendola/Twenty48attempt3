import pygame
pygame.init()
screen = pygame.display.set_mode((100, 100))
screen.fill("gold")
pygame.display.update()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            print("Keydown")
            if event.key == pygame.K_SPACE: 
                print("Space key")
            elif event.key == pygame.K_ESCAPE: 
                print("Escape key")
                running = False