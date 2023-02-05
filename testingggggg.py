# pygame template
from typing import List

import pygame
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT


class ScreenInterface:
    def handle_events(self, events: List[pygame.event.Event]) -> None: ...
    def update(self) -> None: ...
    def draw(self, surface: pygame.Surface) -> None: ...


class PauseScreen:
    def __init__(self, parent: ScreenInterface):
        self.parent = parent

    def handle_events(self, events: List[pygame.event.Event]) -> None:
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    Game.set_screen(self.parent)

    def update(self) -> None:
        pass

    def draw(self, surface: pygame.Surface) -> None:
        self.parent.draw(surface)

        background = pygame.Surface((Game.WIDTH, Game.HEIGHT), pygame.SRCALPHA)
        pygame.draw.rect(background, (0, 0, 0, 128), (0, 0, Game.WIDTH, Game.HEIGHT))

        surface.blit(background, (0, 0))
        pygame.draw.rect(surface, (200, 200, 200), (300, 400, 300, 100))




class ScreenOne:
    def __init__(self) -> None:
        self.circle_x = 200
        self.circle_y = 200
        
    def handle_events(self, events: List[pygame.event.Event]) -> None: 
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # Game.set_screen(ScreenTwo())
                print("Click")
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    Game.set_screen(PauseScreen(self))

    def update(self) -> None: 
        self.circle_x += 1

    def draw(self, surface: pygame.Surface) -> None: 
        surface.fill((255, 255, 255))  # always the first drawing command
        pygame.draw.circle(surface, (0, 0, 255), (self.circle_x, self.circle_y), 30)



class ScreenTwo:
    def __init__(self) -> None:
        self.circle_x = 500
        self.circle_y = 100
        
    def handle_events(self, events: List[pygame.event.Event]) -> None: ...

    def update(self) -> None: 
        self.circle_y += 1
        
    def draw(self, surface: pygame.Surface) -> None: 
        surface.fill((0, 0, 255))  # always the first drawing command
        pygame.draw.circle(surface, (0, 255, 0), (self.circle_x, self.circle_y), 30)



class Game:
    instance: 'Game'
    WIDTH = 640
    HEIGHT = 480
    SIZE = (WIDTH, HEIGHT)

    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode(self.SIZE)
        self.clock = pygame.time.Clock()

        self.current_screen = ScreenOne()

        Game.instance = self
    
    @classmethod
    def set_screen(cls, new_screen: ScreenInterface):
        cls.instance.current_screen = new_screen

    def run(self):
        running = True
        while running:
            # EVENT HANDLING
            events = pygame.event.get()
            for event in events:
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == QUIT:
                    running = False

            self.current_screen.handle_events(events)
            self.current_screen.update()
            self.current_screen.draw(self.screen)

            # Must be the last two lines
            # of the game loop
            pygame.display.flip()
            self.clock.tick(30)

        pygame.quit()


if __name__ == "__main__":
    game = Game()
    game.run()