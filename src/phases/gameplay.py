from typing import TYPE_CHECKING

import pygame as pg
from pygame.constants import (
    K_ESCAPE,
    KEYDOWN,
    MOUSEBUTTONDOWN,
)

from src.classes.town import Town
from src.colors import CORAL, MANTLE
from src.state import Phase, State
from src.utils.logging import setup_logging

if TYPE_CHECKING:
    from src.component import Component

logger = setup_logging()


class Gameplay:
    def __init__(self) -> None:
        self.field_components: list[Component] = []

    def handle_event(self, event: pg.event.Event, state: State) -> None:
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            state.game_phase = Phase.MAIN_MENU
            logger.info("Gameplay -> Mainmenu.")
        elif event.type == MOUSEBUTTONDOWN:
            # Just for testing...
            self.field_components.append(Town(event.pos, 20, CORAL))

    def update(self) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        screen.fill(MANTLE)

        for component in self.field_components:
            component.draw(screen)
