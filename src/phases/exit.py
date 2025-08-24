import sys

import pygame as pg

from src.colors import CRUST
from src.utils.logging import setup_logging

logger = setup_logging()


def exit_phase(screen: pg.Surface) -> None:
    screen.fill(CRUST)
    pg.display.update()

    logger.info("Exiting...")
    pg.quit()
    sys.exit()
