import pygame
import numpy as np
from helpers import radians_to_degrees
from Physics import Controls

class Car:
    def __init__(self, 
                 pos_x: float, 
                 pos_y: float,
                 size_x: float = 30, 
                 size_y: float = 10, 
                 color: tuple = (0, 0, 0)
                 ) -> None:
        
        # TODO: Decide which variables are private/public
        # PUBLIC
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.size_x = size_x
        self.size_y = size_y
        self.color = color

        self.content_surface = pygame.Surface((size_x*2, size_y*2), pygame.SRCALPHA)

        self.max_speed = 3
        self.max_angle = np.pi/3
        self.friction = 0.05
        self.speed = 0
        self.acceleration = 0.2
        self.angle = np.pi/2

        self.controls = Controls()

        # PRIVATE
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
    
    def _rotate(self, display: pygame.display):
        self.content_surface.fill((0, 0, 255, 255)) # clear with tranparent color
        self._draw_car()
        rotated_surface = pygame.transform.rotate(self.content_surface, radians_to_degrees(-self.angle))
        rotated_rect = rotated_surface.get_rect(center=(self.pos_x + self.size_x // 2, self.pos_y + self.size_y // 2))
        display.blit(rotated_surface, rotated_rect)
        
    def _draw_car(self):
        pygame.draw.rect(self.content_surface, self.color, pygame.Rect(self.size_x//2, self.size_y//2, self.size_x, self.size_y))
        pygame.draw.rect(self.content_surface, (0, 255, 0), pygame.Rect(0, 0, self.size_y//2, self.size_y//2))
        pygame.draw.rect(self.content_surface, (0, 255, 0), pygame.Rect(0, 1.5*self.size_y, self.size_y//2, self.size_y//2))
        pygame.draw.rect(self.content_surface, (255, 0, 0), pygame.Rect(1.5*self.size_x + self.size_y, 0, self.size_y//2, self.size_y//2))
        pygame.draw.rect(self.content_surface, (255, 0, 0), pygame.Rect(1.5*self.size_x + self.size_y, 1.5*self.size_y, self.size_y//2, self.size_y//2))

    def draw(self, display: pygame.display):
        self._move()
        self._rotate(display)
