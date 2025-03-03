import math
import random

import pygame
from pygame import Surface

class FixedBackground:
    def __init__(self, surface: Surface, image: Surface):
        self.surface = surface
        self.image = image

        self.old_surface_size = self.surface.get_size()
        self.resize_image()

    def render(self, opacity: float = 1) -> None:
        if self.old_surface_size != self.surface.get_size():
            self.resize_image()

        for index in range(self.tiles):
            self.image.set_alpha(int(255 * opacity))
            self.surface.blit(self.image, (0 + index * self.image.get_width(), 0))

    def resize_image(self) -> None:
        multiplier = self.surface.get_height() / self.image.get_height()
        self.image = pygame.transform.scale_by(self.image, multiplier)
        self.tiles = math.ceil(self.surface.get_width() / self.image.get_width())