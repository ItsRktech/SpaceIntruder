import pygame

# Initialize Pygame
pygame.init() #must used to initialize all pygame modules

# create a window
screen = pygame.display.set_mode((1366, 768))

# Title and Icon
pygame.display.set_caption("Space Intruder")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


#player
playerImg = pygame.image.load('spaceship.png')
playerX = 660
playerY = 638
playerX_change = 0

def player(x,y):
    screen.blit(playerImg, (x, y))
    
#game loop
running = True
while running:
    # Background color #Red Green Blue
    screen.fill((0, 0 ,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
    #if a key is pressed check whether its right or left
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            playerX_change = -0.3
        if event.key == pygame.K_RIGHT:
            playerX_change = +0.3
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            playerX_change = 0
            
    # Updating player position
    playerX += playerX_change
    player(playerX, playerY)        
    pygame.display.update() #must used to update the display surface to the screen


    