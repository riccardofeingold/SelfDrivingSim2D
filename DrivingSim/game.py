import pygame
from objects import Car
from Physics import Controls
class Constants(object):
    WIDTH = 800
    HEIGHT = 600
    FRAME_RATE = 40

class DrivingSim:
    def __init__(self, height: int = Constants.WIDTH, width: int = Constants.HEIGHT, human: bool = True) -> None:
        self.height = height
        self.width = width
        self.human = human

        self.display = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.game_over = False
        self.score = 0
        
        self.controls = Controls()
        self.car = Car(self.width/2, self.height/2)
        
        pass

    def step(self):
        # to allow normal window quitting
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            self.car.controls.keyboard_listener(event)

        # render and move car
        self.render(self.display)

        self.clock.tick(Constants.FRAME_RATE)
        return self.game_over, self.score

    def render(self, display: pygame.display):
        self.display.fill((255, 255, 255))
        self.car.draw(display=display)

        pygame.display.flip()
        pass


if __name__ == "__main__":
    pygame.init()

    game = DrivingSim()

    while True:
        game_over, score = game.step()

        if game_over:
            break
    
    pygame.quit()