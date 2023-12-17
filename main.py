import pygame

pygame.init()
screen = pygame.display.set_mode((300, 300))
ball = pygame.image.load('creature.png')
ballX = 0
ballY = 0
speed = 5
to_left = False
to_right = False
to_up = False
to_down = False
while True:
    screen.fill((255, 255, 255))
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_DOWN:
                to_down = True
            if event.key == pygame.K_UP:
                to_up = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_DOWN:
                to_down = False
            if event.key == pygame.K_UP:
                to_up = False
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if to_right:
        ballX += speed
    if to_left:
        ballX -= speed
    if to_down:
        ballY += speed
    if to_up:
        ballY -= speed
    screen.blit(ball, (ballX, ballY))
    pygame.display.update()
