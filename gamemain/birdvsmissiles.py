import pygame
import random
import sys
#https://realpython.com/pygame-a-primer/#background-and-setup

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
score = 0
score_increment = 1
running = True

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.image.load("gamemain/bird.png").convert()
        self.surf.set_colorkey((0,0,0), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        # Move the sprite based on user keypresses
    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
     if pressed_keys[pygame.K_UP]:
        self.rect.move_ip(0, -5)
     if pressed_keys[pygame.K_DOWN]:
        self.rect.move_ip(0, 5)
     if pressed_keys[pygame.K_LEFT]:
        self.rect.move_ip(-9, 0)
     if pressed_keys[pygame.K_RIGHT]:
        self.rect.move_ip(5, 0)
     if self.rect.left < 0:
        self.rect.left = 0
     if self.rect.right > SCREEN_WIDTH:
        self.rect.right = SCREEN_WIDTH
     if self.rect.top <= 0:
        self.rect.top = 0
     if self.rect.bottom >= SCREEN_HEIGHT:
        self.rect.bottom = SCREEN_HEIGHT

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("gamemain/missile.png").convert()
        self.surf.set_colorkey((255,255,255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect(
            center=(
                random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),
                random.randint(0, SCREEN_HEIGHT),
            )
        )
        self.speed = random.randint(5, 20)
        
    def update(self):
        global score
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()
            score += score_increment

class Cloud(pygame.sprite.Sprite):
    def __init__(self):
      super(Cloud, self).__init__()
      self.surf = pygame.image.load("gamemain/cloud.png").convert()
      self.surf.set_colorkey((0,0,0), pygame.RLEACCEL)
      self.rect = self.surf.get_rect(
         center = (
            random.randint(SCREEN_WIDTH, SCREEN_WIDTH + 100), random.randint(0, SCREEN_HEIGHT),
         )
      )
    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)
player = Player()
enemies = pygame.sprite.Group()
clouds = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
clock = pygame.time.Clock()
start = 1800
clock = pygame.time.Clock()
start_time = pygame.time.get_ticks()  # Get the start time in milliseconds
elapsed_time = 0  # Initialize the elapsed time to 0
time_interval = 10
#-----------FONT----------
font = pygame.font.Font('PixelifySans-Regular.ttf', 48)

while running:
    # Did the user click the window close button?

    for event in pygame.event.get():
        pressed_keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)
        elif event.type == ADDCLOUD:
           new_cloud = Cloud()
           clouds.add(new_cloud)
           all_sprites.add(new_cloud)
    player.update(pressed_keys)
    enemies.update()
    clouds.update()

    current_time = pygame.time.get_ticks() // 1000  # Current time in seconds
    # Check if it's time to change the speed
    if current_time - elapsed_time >= time_interval:
        # Update the speed of all enemies
        for enemy in enemies:
            enemy.speed += 5  # New random speed between 10 and 30

        # Update the last speed change time
        elapsed_time = current_time


    # Fill background blue
    screen.fill((140, 205, 250))
    for entity in all_sprites:
      screen.blit(entity.surf, entity.rect)
    if pygame.sprite.spritecollideany(player, enemies):
       player.kill()
       running = False
    
     # Check for collisions
    if pygame.sprite.spritecollideany(player, enemies):
       player.kill()
       running = False
       
    #whem rocket passes left edge increment score
    for enemy in enemies: 
        if enemy.rect.right < 0:
           score += 5
           enemy.kill()

    #display score 
    score_text = font.render(f'Score: {score}', True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

   
    pygame.display.flip()
    clock.tick(30)

   
    

# Done! Time to quit.
pygame.quit()
                                 
                             
                    
