import math
import random

import pygame
from pygame import Surface

class ParallaxBackground:
    def __init__(self, surface: Surface, images: list[Surface], ratio: float = 1):
        self.surface = surface
        self.images = images
        self.ratio = ratio

        self.parallax_stack = []

        self.old_surface_size = self.surface.get_size()
        self.resize_images()

    def render(self, absolute_position: int = 0, opacity: float = 1) -> None:
        if self.old_surface_size != self.surface.get_size(): 
            self.resize_images()

        absolute_position *= self.ratio
        while len(self.parallax_stack) < self.tiles:
            last_position = self.parallax_stack[-1][0] if self.parallax_stack else absolute_position
            self.parallax_stack.append((
                last_position + self.images[0].get_width(), 
                self.images[random.randint(0, len(self.images) - 1)]
            ))

        if self.parallax_stack[0][0] + self.images[0].get_width() < absolute_position:
            self.parallax_stack.pop(0)

        for position, element in self.parallax_stack:
            element.set_alpha(int(255 * opacity))
            self.surface.blit(element, (position - absolute_position - self.images[0].get_width(), 0))

    def resize_images(self):
        multiplier = self.surface.get_height() / self.images[0].get_height()
        for index, image in enumerate(self.images):
            self.images[index] = pygame.transform.scale_by(image, multiplier)

        for index, (position, image) in enumerate(self.parallax_stack):
            self.parallax_stack[index] = (position * multiplier - 2 * self.images[0].get_width(), pygame.transform.scale_by(image, multiplier))

        self.tiles = math.ceil(2 + self.surface.get_width() / self.images[0].get_width())
        self.old_surface_size = self.surface.get_size()