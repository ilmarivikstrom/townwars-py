import pygame as pg
from pygame.locals import K_RETURN, KEYDOWN, QUIT, K_q

from src.colors import GRAY20
from src.state import Phase, State
from src.utils.logging import setup_logging

logger = setup_logging()


def mainmenu_phase(state: State, screen: pg.Surface) -> None:
    screen.fill(GRAY20)
    for event in pg.event.get():
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_q):
            state.game_phase = Phase.EXIT
            logger.info("Mainmenu -> Exit.")
            return
        if event.type == KEYDOWN and event.key == K_RETURN:
            state.game_phase = Phase.GAMEPLAY
            logger.info("Mainmenu -> Gameplay.")
