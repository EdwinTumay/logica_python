import pygame
import math
from abc import ABC, abstractclassmethod

class CelestialObject(ABC):
    def __init__(self, image_path, mass, distance = 0, orbit_speed = 0):
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.angle = 0
        self.distance = distance
        self.mass = mass
        self._orbit_speed = 0

        self._orbit_speed = orbit_speed

    @property
    def orbit_speed(self):
        return self._orbit_speed
    
    @orbit_speed.setter
    def orbit_speed(self, value):
        if value >= 1 and value <= 10:
            self._orbit_speed = value
        else:
            raise ValueError('Orbit value error')

    def update(self):
        self.angle += self.orbit_speed

    def draw(self, screen):
        x  = (screen.get_width() //2) + (self._distance * math.cos(math.radians(self._angle)))
        y  = (screen.get_height() //2) + (self._distance * math.sin(math.radians(self._angle)))
        self.rect.centerx = x
        self.rect.centery = y
        screen.blit(self.image, self.rect)

    @abstractclassmethod
    def generate_magnetic_field(self, screen):
        pass