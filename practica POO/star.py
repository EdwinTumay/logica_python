import pygame
from celestial_object import CelestialObject

class Star(CelestialObject):
    def __init__(self, image_path, mass, nucleo_status):
        super().__init__(image_path= image_path, mass=mass)

    def generate_magnetic_field(self, screen):
        if self.nucleo_status == 'Active' and self.mass > 1000:
            width = self.rect.width + 40
            height = self.rect.height + 40
            blue_field = pygame.imagen.load('campo_rojo.png')
            blue_field_resized = pygame.transform.scale(blue_field, 
                                                        (width, 
                                                        height))
            blue_field_resized_rect = blue_field_resized.get_rect()
            blue_field_resized_rect.centerx = self.react.centerx
            blue_field_resized_rect.centery = self.react.centery
            screen.blit(blue_field_resized, blue_field_resized_rect)
