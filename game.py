import sys
import pygame

from background import FixedBackground
from background import ParallaxBackground

class Game:
    running: bool = False
    position: float = 0

    def __init__(self, width: int, height: int):
        pygame.init()

        self.width = width
        self.height = height

        self.delta = 0
        self.clock = pygame.time.Clock()

        self.surface = pygame.display.set_mode(self.size, pygame.RESIZABLE, 32)
        pygame.display.set_caption("Uprising - Keep Moving Forward!")
        pygame.display.set_icon(pygame.image.load("./assets/uprising.png").convert_alpha())

        self.load_backgrounds()

    def run(self) -> None:
        self.running = True

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.VIDEORESIZE:
                    self.width = event.w
                    self.height = event.h
                    continue

                if event.type == pygame.QUIT:
                    self.running = False

            self.position += 200 * self.delta

            self.render_backgrounds()
            self.render_foregrounds()
            
            font = pygame.font.SysFont("Arial", 18, bold=True)
            fps = font.render("fps: " + str(int(self.clock.get_fps())), 1, pygame.Color("WHITE"))
            self.surface.blit(fps, (10, 10))

            pygame.display.flip()

            self.delta = self.clock.tick(60) / 1000

        pygame.quit()

    def load_backgrounds(self) -> None:
        self.sky = FixedBackground(self.surface, 
            pygame.image.load("./assets/sky.png").convert_alpha()
        )

        self.city_back = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/city/back/city-1.png").convert_alpha(),
            pygame.image.load("./assets/city/back/city-2.png").convert_alpha(),
        ], .2)

        self.city_middle = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/city/middle/city-1.png").convert_alpha(),
            pygame.image.load("./assets/city/middle/city-2.png").convert_alpha(),
            pygame.image.load("./assets/city/middle/city-3.png").convert_alpha(),
        ], .4)

        self.city_front = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/city/front/city-1.png").convert_alpha(),
            pygame.image.load("./assets/city/front/city-2.png").convert_alpha(),
            pygame.image.load("./assets/city/front/city-3.png").convert_alpha(),
            pygame.image.load("./assets/city/front/city-4.png").convert_alpha(),
        ], .6)

        self.clouds_back = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/clouds/back/clouds-1.png").convert_alpha(),
            pygame.image.load("./assets/clouds/back/clouds-2.png").convert_alpha(),
            pygame.image.load("./assets/clouds/back/clouds-3.png").convert_alpha(),
        ], .3)

        self.clouds_front = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/clouds/front/clouds-1.png").convert_alpha(),
            pygame.image.load("./assets/clouds/front/clouds-2.png").convert_alpha(),
            pygame.image.load("./assets/clouds/front/clouds-3.png").convert_alpha(),
        ], .5)

        self.barrier_back = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/barriers/back/barrier-1.png").convert_alpha(),
            pygame.image.load("./assets/barriers/back/barrier-2.png").convert_alpha(),
            pygame.image.load("./assets/barriers/back/barrier-3.png").convert_alpha(),
            pygame.image.load("./assets/barriers/back/barrier-4.png").convert_alpha(),
            pygame.image.load("./assets/barriers/back/barrier-5.png").convert_alpha(),
        ], 2)

        self.barrier_front = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/barriers/front/barrier-1.png").convert_alpha(),
            pygame.image.load("./assets/barriers/front/barrier-2.png").convert_alpha(),
            pygame.image.load("./assets/barriers/front/barrier-3.png").convert_alpha(),
        ], 3)

        self.road = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/road/road-1.png").convert_alpha(),
            pygame.image.load("./assets/road/road-2.png").convert_alpha(),
            pygame.image.load("./assets/road/road-3.png").convert_alpha(),
        ], 2.2)

        self.sidewalk = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/sidewalks/sidewalk-1.png").convert_alpha(),
            pygame.image.load("./assets/sidewalks/sidewalk-2.png").convert_alpha(),
            pygame.image.load("./assets/sidewalks/sidewalk-3.png").convert_alpha(),
        ], 2.1)

    def render_backgrounds(self) -> None:
        self.sky.render()

        self.clouds_back.render(int(self.position), .75)
        self.city_back.render(int(self.position), .85)
        self.city_middle.render(int(self.position), .95)
        self.clouds_front.render(int(self.position), .9)
        self.city_front.render(int(self.position))

        self.barrier_back.render(int(self.position))
        self.sidewalk.render(int(self.position))
        self.road.render(int(self.position))

    def render_foregrounds(self) -> None:
        self.barrier_front.render(int(self.position))
    
    @property
    def size(self) -> tuple:
        return self.width, self.height