import pygame

class Controls:
    def __init__(self) -> None:
        self.forward = False
        self.left = False
        self.right = False
        self.backward = False
        self.mouse_down = [False, False, False] # left, middle, right
    
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
    
    def mouse_listener(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.mouse.get_pressed()[0]: # Left Click
                self.mouse_down[0] = True
            elif pygame.mouse.get_pressed()[1]: # Middle Click
                self.mouse_down[1] = True
            elif pygame.mouse.get_pressed()[2]: # Right Click
                self.mouse_down[2] = True