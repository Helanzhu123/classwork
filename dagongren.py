#when calling a function or a class must follow with ()
import pygame
import random
import pathlib

pygame.init()

window_height = 600
window_width = 800
window = pygame.display.set_mode((window_width, window_height)) 

image_folder = pathlib.Path(__file__).parent/"resource/img"
player_image = pygame.image.load(str(image_folder/"santaclause.png")).convert_alpha() #convert_alpha = make game more smooth
background_image = pygame.image.load(str(image_folder/"christmas.jpg")).convert()
gift_image = pygame.image.load(str(image_folder/"christmasbox.png")).convert_alpha()

pygame.display.set_caption("Christmas Game")

#RGB: Red:0-255 Green: 0-255 Blue: 0-255
FPS = 60
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
light_green = (0,250,154)
blue = (0, 0, 255)
dark_blue = (25,25,112)
pink = (255, 192, 203)

class Player(pygame.sprite.Sprite):   #sprite = character
    def __init__(self): # self is always the first parameter in method
        super().__init__() #important as fck: initialize parent class
        # self.image = pygame.Surface((50, 50))
        # self.image.fill(light_green)
        self.image = pygame.transform.scale(player_image, (50,80))
        self.rect = self.image.get_rect()        
        self.rect.centerx = window_width//2
        self.rect.bottom = window_height - 30
        self.speed = 5
    
    def update(self): #when certain event happens, use this method to update position, color, etc.
        keys = pygame.key.get_pressed()
        # if keys[pygame.K_w] or keys[pygame.K_UP]:
        #     self.rect.y -= self.speed
        # if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        #     self.rect.y += self.speed
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rect.x += self.speed

        if self.rect.bottom > window_height:
            self.rect.bottom = window_height
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > window_width:
            self.rect.right = window_width
        
class Gift(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.spawn()
        # self.image = pygame.Surface((30, 30))
        # self.image.fill(red)
    def spawn(self):
        self.size = random.randint(10, 40)
        self.image = pygame.transform.scale(gift_image, (self.size, self.size))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, window_width)
        self.rect.y = random.randint(-200, -10)

    def update(self):
        self.rect.y += 5
        if self.rect.top > window_height:
            self.spawn()

player = Player()
sprite_group = pygame.sprite.Group() # to update everything in the group
sprite_group.add(player)
gift_group = pygame.sprite.Group()
for i in range(10):
    gift = Gift()
    sprite_group.add(gift)
    gift_group.add(gift)

clock = pygame.time.Clock() # class need a variable to hold
game_running = True
points = 0
while game_running:      
    
    # pygame.time.wait(100) #ugly way
    clock.tick(FPS)
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: #QUIT data
            game_running = False
        # elif event.type == pygame.KEYDOWN:
        #     if event.key == pygame.K_a:
        #         print("yay")
    
    sprite_group.update()
    touched_gifts = pygame.sprite.spritecollide(player, gift_group, True)
    for i in touched_gifts:
        points += 10
        print(f"Score: {points}")

    # window.fill(dark_blue)
    window.blit(background_image, background_image.get_rect()) #blit = copy
    sprite_group.draw(window)

    pygame.display.flip()

pygame.quit()
print("Thank you for playing this game, bye bye!")
