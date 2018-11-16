import sys, pygame
pygame.init()

size = width, height = 1500, 1000
speed = [50, 50]
bg = 0x1c, 0x81, 0xf2

screen = pygame.display.set_mode(size)

ball = pygame.image.load("EnderdragonFlying.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(bg)
    screen.blit(ball, ballrect)
    pygame.display.flip()
