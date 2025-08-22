import pygame as pg

from src.utils.logging import setup_logging

logger = setup_logging()


def main() -> None:
    numpass, numfail = pg.init()
    logger.debug(f"pygame loaded! Modules passed: {numpass}, modules failed: {numfail}")
    pg.print_debug_info()

    from src.game_loop import GameLoop  # noqa: PLC0415

    game_loop = GameLoop()
    game_loop.loop()


if __name__ == "__main__":
    main()
