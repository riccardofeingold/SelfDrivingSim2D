import numpy as np

class Vector():
    def __init__(self, init_x: float = 0, init_y: float = 0) -> None:
        self.x: float = init_x
        self.y: float = init_y

# MATH methods
def radians_to_degrees(radians: float):
    return radians * 180 / np.pi

def degrees_to_radians(degrees: float):
    return degrees * np.pi / 180