import pygame

class Controls:
    def __init__(self) -> None:
        self.forward = False
        self.left = False
        self.right = False
        self.backward = False
    
    def keyboard_listener(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.left = True
            if event.key == pygame.K_RIGHT:
                self.right = True
            if event.key == pygame.K_UP:
                self.forward = True
            if event.key == pygame.K_DOWN:
                self.backward = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.left = False
            if event.key == pygame.K_RIGHT:
                self.right = False
            if event.key == pygame.K_UP:
                self.forward = False
            if event.key == pygame.K_DOWN:
                self.backward = False