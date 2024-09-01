import pygame
import numpy as np
from Physics import Controls
from helpers import Vector

class Road:
    def __init__(self, width) -> None:
        # TODO: use order list. Order points according to closeness
        self.points = []
        self.width = width
        self.closed = False

        self.controls = Controls()
        pass

    def add_remove_points(self):
        if self.controls.mouse_down[0]:
            self.points.append(pygame.mouse.get_pos())
            self.controls.mouse_down[0] = False
        
        if self.points.__len__() > 0 and self.controls.mouse_down[2]:
            mouse_pos = np.array(pygame.mouse.get_pos())

            min_distance = 100000
            min_index = 0
            index = 0
            for p in self.points:
                distance = np.linalg.norm(mouse_pos - np.array(p))
                if min_distance > distance:
                    min_distance = distance
                    min_index = index
                index += 1
            
            del self.points[min_index]
            self.controls.mouse_down[2] = False


    def draw(self, display: pygame.display):
        self.add_remove_points()

        if self.controls.mouse_down[1]:
            self.closed = not self.closed
            self.controls.mouse_down[1] = False

        if self.points.__len__() > 1:
            pygame.draw.lines(display, color=pygame.Color(255, 0, 0), points=self.points, width=3, closed=self.closed)
        elif self.points.__len__() == 1:
            pygame.draw.circle(display, color=pygame.Color(255, 0, 0), radius=2, center=self.points[0])
        pass