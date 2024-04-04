import pygame
import numpy as np
from Physics import Controls

class Vector():
    def __init__(self, init_x: float = 0, init_y: float = 0) -> None:
        self.x: float = init_x
        self.y: float = init_y

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

        self.surface = pygame.Surface((size_x, size_y))
        self.surface.fill(color)
        self.rect = self.surface.get_rect()
        self.rect.center = (self.size_x//2, self.size_y//2)

        self.max_speed = 3
        self.max_angle = np.pi/3
        self.friction = 0.05
        self.speed = 0
        self.acceleration = 0.2
        self.angle = np.pi/2

        self.controls = Controls()
        pass

    def _move(self):
        if self.controls.forward:
            self.speed -= self.acceleration
        if self.controls.backward:
            self.speed += self.acceleration
        
        if self.speed != 0:
            flip = -1 if self.speed > 0 else 1
            if self.controls.left:
                self.angle -= 0.03*flip
            if self.controls.right:
                self.angle += 0.03*flip
        
        # set maximum speed
        if self.speed < -self.max_speed:
            self.speed = -self.max_speed
        
        if self.speed > self.max_speed / 2:
            self.speed = self.max_speed / 2

        # add friction
        if self.speed > 0:
            self.speed -= self.friction
        
        if self.speed < 0:
            self.speed += self.friction
        
        if abs(self.speed) < self.friction:
            self.speed = 0

        self.pos_y += self.speed * np.sin(self.angle)
        self.pos_x += self.speed * np.cos(self.angle)
    
    def rotate(self):
        self.surface = pygame.transform.rotate(self.surface, self.angle)
        self.rect = self.surface.get_rect()
        self.rect.center = (self.pos_x, self.pos_y)

    def draw(self, display: pygame.display):
        self._move()
        # self.rotate()
        # display.blit(self.surface, self.rect)
        pygame.draw.rect(display, self.color, pygame.Rect(self.pos_x, self.pos_y, self.size_x, self.size_y))
