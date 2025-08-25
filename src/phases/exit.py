import sys

import pygame as pg

from src.colors import CRUST
from src.state import State
from src.utils.logging import setup_logging

logger = setup_logging()


class Exit:
    def __init__(self) -> None:
        pass

    def handle_event(self, event: pg.event.Event, state: State) -> None:
        pass

    def update(self) -> None:
        logger.info("Exiting...")

    def draw(self, screen: pg.Surface) -> None:
        screen.fill(CRUST)
        pg.display.update()
        pg.quit()
        sys.exit()
