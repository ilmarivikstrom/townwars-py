import sys

import pygame as pg

from src.utils.logging import setup_logging

logger = setup_logging()


def exit_phase() -> None:
    logger.info("Exiting...")
    pg.quit()
    sys.exit()
