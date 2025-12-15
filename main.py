import pygame
import math
import random
from pygame import mixer

# Initialize Pygame
pygame.init() #must used to initialize all pygame modules

# create a window
screen = pygame.display.set_mode((800, 600))

#background
background = pygame.image.load('bg.png')

#background sound
mixer.music.load('background.mp3')
mixer.music.set_volume(0.1)
mixer.music.play(-1)

# Title and Icon
pygame.display.set_caption("Space Intruder")
icon = pygame.image.load('ufo.png')
pygame.display.set_icon(icon)


#player
playerImg = pygame.image.load('spaceship.png')
playerX = 395
playerY = 490
playerX_change = 0


#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('enemy.png'))
    enemyX.append(random.randint(0, 736))
    enemyY.append(random.randint(50, 50))
    enemyX_change.append(4)
    enemyY_change.append(40)

#bullet
bulletImg = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 490
bulletX_change = 0
bulletY_change = 7
bullet_state = "ready" #ready - you can't see the bullet on the screen / fire - the bullet is currently moving

# score

score = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textX = 10
textY = 10

#game over font
over_font = pygame.font.Font('freesansbold.ttf', 64)

def show_score(x, y):
    score_value = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score_value, (x, y))
    
def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255, 255, 255))
    screen.blit(over_text, (225, 250))
def player(x,y):
    screen.blit(playerImg, (x, y))
    
def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))
    
#fire bullet
def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2)) + (math.pow(enemyY - bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
    
#game loop
running = True
while running:
    # Background color #Red Green Blue
    screen.fill((0, 0 ,0))
    
    # Background Image
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        #if a key is pressed check whether its right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -0.5
            if event.key == pygame.K_RIGHT:
                playerX_change = +0.5
            if event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_Sound = mixer.Sound('laser.wav')
                    bullet_Sound.play()
                    bulletX = playerX
                    bulletY = playerY
                    bullet_state = "fire"
            
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
            
    # Updating player position
    playerX += playerX_change
    
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736: #800-64(width of spaceship)
        playerX = 736
        
    # Updating enemy position
    for i in range(num_of_enemies):
        
        #Game Over
        if enemyY[i] > 420:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break
                                                                          
        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 0.5
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -0.5
            enemyY[i] += enemyY_change[i]
        
        # Collision
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_Sound = mixer.Sound('explosion.wav')
            explosion_Sound.play()
            bulletY = 490
            bullet_state = "ready"
            score += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(50, 150)
        enemy(enemyX[i], enemyY[i], i)    
    # Bullet Movement
    if bulletY <= 0:
            bulletY = 490
            bullet_state = "ready"
            
    if bullet_state == "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
    
    
        
    player(playerX, playerY)         
    show_score(textX, textY)             
    pygame.display.update() #must used to update the display surface to the screen


    