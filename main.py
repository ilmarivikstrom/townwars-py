import pygame as pg

from src.colors import CORNFLOWERBLUE
from src.config import Config
from src.utils.logging import setup_logging

logger = setup_logging()


def main() -> None:
    numpass, numfail = pg.init()
    logger.debug(f"pygame loaded! Modules passed: {numpass}, modules failed: {numfail}")
    pg.print_debug_info()

    clock = pg.time.Clock()

    pg.display.set_caption(Config.TITLE_CAPTION)
    screen_surf = pg.display.set_mode((Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT))
    screen_surf.fill(CORNFLOWERBLUE)  # memes

    should_continue = True

    current_tick: int = 0

    while should_continue:
        for event in pg.event.get():
            if event.type == pg.QUIT or (
                event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE
            ):
                should_continue = False
                break
        pg.display.update()
        _ = clock.tick(60)

        current_tick += 1
        if current_tick % 100 == 0:
            logger.debug(f"FPS: {clock.get_fps()}")

    logger.debug("Quit condition met, exiting...")
    pg.quit()


if __name__ == "__main__":
    main()
