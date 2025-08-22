import pygame as pg

from src.config import Config
from src.phases.exit import exit_phase
from src.phases.gameplay import gameplay_phase
from src.phases.mainmenu import mainmenu_phase
from src.phases.phase import Phase
from src.state import State
from src.utils.logging import setup_logging

logger = setup_logging()


class GameLoop:
    def __init__(self) -> None:
        self.screen: pg.Surface = pg.display.set_mode(
            (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT),
        )
        self.state = State()
        pg.display.set_caption(Config.TITLE_CAPTION)
        self.clock = pg.time.Clock()
        logger.info("Gameloop initialized.")

    def loop(self) -> None:
        while True:
            if self.state.game_phase == Phase.MAIN_MENU:
                mainmenu_phase(self.state, self.screen)
            elif self.state.game_phase == Phase.EXIT:
                exit_phase()
            elif self.state.game_phase == Phase.GAMEPLAY:
                gameplay_phase(self.state, self.screen)

            self.state.current_tick += 1
            pg.display.update()
            self.clock.tick(60)
