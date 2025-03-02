import sys
import pygame

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
        
        self.front_barrier = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/barriers/front/barrier-1.png").convert_alpha(),
            pygame.image.load("./assets/barriers/front/barrier-2.png").convert_alpha(),
            pygame.image.load("./assets/barriers/front/barrier-3.png").convert_alpha(),
        ], 3)

        self.road = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/road/road-1.png").convert_alpha(),
            pygame.image.load("./assets/road/road-2.png").convert_alpha(),
            pygame.image.load("./assets/road/road-3.png").convert_alpha(),
        ], 2.1)

        self.sidewalk = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/sidewalks/sidewalk-1.png").convert_alpha(),
            pygame.image.load("./assets/sidewalks/sidewalk-2.png").convert_alpha(),
            pygame.image.load("./assets/sidewalks/sidewalk-3.png").convert_alpha(),
        ], 2.05)

        self.barrier = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/barriers/back/barrier-1.png").convert_alpha(),
            pygame.image.load("./assets/barriers/back/barrier-2.png").convert_alpha(),
            pygame.image.load("./assets/barriers/back/barrier-3.png").convert_alpha(),
            pygame.image.load("./assets/barriers/back/barrier-4.png").convert_alpha(),
            pygame.image.load("./assets/barriers/back/barrier-5.png").convert_alpha(),
        ], 2)

        self.foreground_clouds = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/clouds/clouds-1a.png").convert_alpha(),
            pygame.image.load("./assets/clouds/clouds-1b.png").convert_alpha(),
            pygame.image.load("./assets/clouds/clouds-1c.png").convert_alpha(),
        ], .6)

        self.background_clouds = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/clouds/clouds-2a.png").convert_alpha(),
            pygame.image.load("./assets/clouds/clouds-2b.png").convert_alpha(),
            pygame.image.load("./assets/clouds/clouds-2c.png").convert_alpha(),
        ], .32)

        self.city_background = ParallaxBackground(self.surface, [
            pygame.image.load("./assets/city/city-background-1.png").convert_alpha(),
            pygame.image.load("./assets/city/city-background-2.png").convert_alpha(),
            pygame.image.load("./assets/city/city-background-3.png").convert_alpha(),
        ], .5)


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

            # self.surface.fill("#499ee5")
            self.surface.fill("#48668e")

            self.background_clouds.render(int(self.position), .5)
            self.city_background.render(int(self.position), .95)
            self.foreground_clouds.render(int(self.position), .9)
            self.barrier.render(int(self.position))
            self.sidewalk.render(int(self.position))
            self.road.render(int(self.position))
            self.front_barrier.render(int(self.position))

            font = pygame.font.SysFont("Arial", 18, bold=True)
            fps = font.render("fps: " + str(int(self.clock.get_fps())), 1, pygame.Color("WHITE"))
            self.surface.blit(fps, (10, 10))

            pygame.display.flip()

            self.delta = self.clock.tick(60) / 1000

        pygame.quit()

    @property
    def size(self) -> tuple:
        return self.width, self.height