import pygame as pg
from pygame.constants import (
    K_ESCAPE,
    KEYDOWN,
)

from src.colors import CORNFLOWERBLUE
from src.state import Phase, State
from src.utils.logging import setup_logging

logger = setup_logging()


def gameplay_phase(state: State, screen: pg.Surface) -> None:
    screen.fill(CORNFLOWERBLUE)  # memes

    for event in pg.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            state.game_phase = Phase.MAIN_MENU
            logger.info("Gameplay -> Mainmenu.")
