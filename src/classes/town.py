import pygame as pg

from src.colors import RGB
from src.component import Component


class Town(Component):
    def __init__(
        self,
        position: tuple[int, int],
        radius: int,
        color: RGB,
    ) -> None:
        self.position = position
        self.radius = radius
        self.color = color

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
