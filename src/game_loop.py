import pygame as pg

from src.config import Config
from src.phases.exit import exit_phase
from src.phases.gameplay import gameplay_phase
from src.phases.mainmenu import mainmenu_phase
from src.phases.phase import Phase
from src.state import State
from src.ui.text_display import TextDisplay
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

    def _update_displays(self, phase: Phase) -> None:
        fps_text = f"frame: {self.state.current_frame}\nfps: {self.clock.get_fps():.1f}\ntime: {pg.time.get_ticks() / 1000:.1f}s\ndt: {self.clock.get_time():.1f}ms"  # noqa: E501
        self.fps_display.set_text(fps_text)
        self.fps_display.draw(self.screen)

        if phase == Phase.MAIN_MENU:
            self.phase_display.set_text(
                "Phase: Main Menu\n\nPress ENTER to start\nPress Q to quit",
            )
        elif phase == Phase.GAMEPLAY:
            self.phase_display.set_text(
                "Phase: Gameplay\n\nPress ESC to return to main menu",
            )
        else:
            pass
        self.phase_display.draw(self.screen)

    def loop(self, fps: int = 60) -> None:
        self.fps_display = TextDisplay(
            origin=(20, 20),
            font_size=16,
            padding=10,
            max_width=200,
            background_alpha=180,
        )

        self.phase_display = TextDisplay(
            origin=(20, 120),
            font_size=18,
            padding=12,
            max_width=400,
            background_alpha=180,
        )

        while True:
            if self.state.game_phase == Phase.MAIN_MENU:
                mainmenu_phase(self.state, self.screen)
            elif self.state.game_phase == Phase.EXIT:
                exit_phase()
            elif self.state.game_phase == Phase.GAMEPLAY:
                gameplay_phase(self.state, self.screen)

            self._update_displays(self.state.game_phase)

            self.state.current_frame += 1
            pg.display.update()
            self.clock.tick(fps)
