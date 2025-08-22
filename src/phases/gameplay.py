import pygame as pg
from pygame.constants import (
    K_ESCAPE,
    KEYDOWN,
)

from src.colors import CORNFLOWERBLUE
from src.config import Config
from src.state import Phase, State
from src.utils.logging import setup_logging

logger = setup_logging()


def gameplay_phase(state: State, screen: pg.Surface) -> None:
    pg.display.set_caption(f"{Config.TITLE_CAPTION} - GAMEPLAY")
    screen.fill(CORNFLOWERBLUE)  # memes
    for event in pg.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            state.game_phase = Phase.MAIN_MENU
            logger.info("Gameplay -> Mainmenu.")
