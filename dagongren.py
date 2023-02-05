import pygame
import random

window_height = 600
window_width = 800
window = pygame.display.set_mode((window_width, window_height), pygame.FULLSCREEN) 



pygame.display.set_caption("Christmas Game")

#RGB: Red:0-255 Green: 0-255 Blue: 0-255

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
light_green = (0,250,154)
blue = (0, 0, 255)
dark_blue = (25,25,112)
pink = (255, 192, 203)

snow_flakes = []
for q in range(100):
    x = random.randrange(0, 1110)
    y = random.randrange(0, 590)
    snow_flakes.append([x, y])

class Player(pygame.sprite.Sprite):   #sprite = character
    def __init__(self): # self is always the first parameter in method
        super().__init__() #important as fck: initialize parent class
        self.image = pygame.Surface((50, 50))
        self.rect = self.image.get_rect()
        self.image.fill(light_green)
        self.rect.centerx = window_width//2
        self.rect.centery = window_height//2
    
    def update(self): #when certain event happens, use this method to update position, color, etc.
        pass

player = Player()
sprite_group = pygame.sprite.Group() # to update everything in the group
sprite_group.add(player)

clock = pygame.time.Clock() # class need a variable to hold
game_running = True
while game_running:
    play_mouse_pos = pygame.mouse.get_pos()

    play_text = ge
    # pygame.time.wait(100) #ugly way
    clock.tick(60)
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT: #QUIT data
            game_running = False
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         print("yay")
    
    sprite_group.update()

    window.fill(dark_blue)
    sprite_group.draw(window)

    pygame.display.flip()
