import pygame as pg
from pygame.constants import (
    K_ESCAPE,
    KEYDOWN,
)

from src.colors import CORAL
from src.state import Phase, State
from src.utils.logging import setup_logging

logger = setup_logging()


class Editor:
    def __init__(self) -> None:
        pass

    def handle_event(self, event: pg.event.Event, state: State) -> None:
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            logger.info("Editor -> Mainmenu.")
            state.game_phase = Phase.MAIN_MENU

    def update(self) -> None:
        pass

    def draw(self, screen: pg.Surface) -> None:
        screen.fill(CORAL)
