import pygame

class Car:
    def __init__(self, 
                 pos_x: float, 
                 pos_y: float, 
                 size_x: float = 10, 
                 size_y: float = 30, 
                 color: tuple = (0, 0, 0)) -> None:
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color
        pass

    def move(self):
        
        pass

    def draw(self, display: pygame.display):
        pygame.draw.rect(display, self.color, pygame.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y))
