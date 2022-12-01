import pygame

window_width = 800
window_height = 600
pygame.display.set_mode((window_width,window_height)) #{} means it is a package/folder #this is a tuple]
clock = pygame.time.Clock() #clock data type is object of Clock
game_running = True
while game_running:
    clock.tick(60) #Framerate how much time does it refresh. FPS stands for frames per second
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT: 
            game_running = False
    pygame.display.flip() #we have 2 windows, one showing, one drawing behind the screen. flip() is for changing those 2
