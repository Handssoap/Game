import pygame
#https://realpython.com/pygame-a-primer/#background-and-setup

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


running = True
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.Surface((75, 25))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect()
        # Move the sprite based on user keypresses
    # Move the sprite based on user keypresses
    def update(self, pressed_keys):
     if pressed_keys[pygame.K_UP]:
        self.rect.move_ip(0, -5)
     if pressed_keys[pygame.K_DOWN]:
        self.rect.move_ip(0, 5)
     if pressed_keys[pygame.K_LEFT]:
        self.rect.move_ip(-5, 0)
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
pygame.init()

screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
player = Player()

while running:

    # Did the user click the window close button?
    for event in pygame.event.get():
        pressed_keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.KEYUP:
               pygame.draw.circle((0, 4, 2))
    b b 
    player.update(pressed_keys)
    # Fill background blue
    screen.fill((0, 0, 255))
    
    screen.blit(player.surf, player.rect)
    pygame.display.flip()


# Done! Time to quit.
pygame.quit()
                                 
                    
