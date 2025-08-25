import pygame as pg
from pygame.constants import (
    K_ESCAPE,
    KEYDOWN,
)

from src.colors import MANTLE
from src.state import Phase, State
from src.utils.logging import setup_logging

logger = setup_logging()


class Gameplay:
    def __init__(self) -> None:
        pass

    def handle_event(self, event: pg.event.Event, state: State) -> None:
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            state.game_phase = Phase.MAIN_MENU
            logger.info("Gameplay -> Mainmenu.")

    def update(self) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        screen.fill(MANTLE)
