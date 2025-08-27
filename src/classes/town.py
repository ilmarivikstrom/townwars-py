import pygame as pg

from src.colors import RGB
from src.component import Component

font = pg.font.SysFont('Times New Roman', 14, True)

class Town(Component):
    def __init__(
        self,
        position: tuple[int, int],
        radius: int,
        color: RGB,
    ) -> None:
        self.position = position
        self.position_nudge = (self.position[0] - 4, self.position[1] - 7)
        self.radius = radius
        self.color = color
        self.population = 0

    def handle_event(self, event: pg.event.Event) -> None:
        pass

    def update(self) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        pg.draw.circle(screen, self.color, self.position, self.radius - 1)
        pg.draw.aacircle(
            screen,
            (
                self.color.red // 2,
                self.color.green // 2,
                self.color.blue // 2,
            ),
            self.position,
            self.radius,
            3,
        )
        text_surface = font.render(str(self.population), True, (0, 0, 0))
        screen.blit(text_surface, self.position_nudge)
