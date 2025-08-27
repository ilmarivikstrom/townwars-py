import pygame as pg

from src.config import Config
from src.phases.editor import Editor
from src.phases.exit import Exit
from src.phases.gameplay import Gameplay
from src.phases.mainmenu import MainMenu
from src.phases.phase import Phase
from src.state import State
from src.ui.text_display import TextDisplay
from src.utils.logging import setup_logging

logger = setup_logging()


class GameLoop:
    def __init__(self) -> None:
        pg.display.set_caption(Config.TITLE_CAPTION)
        self.screen: pg.Surface = pg.display.set_mode(
            (Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT),
        )
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
        self.state = State()

        self.clock = pg.time.Clock()
        logger.info("Gameloop initialized.")

        self.mainmenu = MainMenu()
        self.gameplay = Gameplay()
        self.editor = Editor()
        self.exit = Exit()

    def _update_debug_displays(self) -> None:
        fps_text = f"frame: {self.state.current_frame}\nfps: {self.clock.get_fps():.1f}\ntime: {pg.time.get_ticks() / 1000:.1f}s\ndt: {self.clock.get_time():.1f}ms"  # noqa: E501
        self.fps_display.set_text(fps_text)
        self.fps_display.draw(self.screen)

        if self.state.game_phase == Phase.MAIN_MENU:
            self.phase_display.set_text(
                "Phase: Main Menu\n\n"
                "Press ENTER to start\n"
                "Press E to open editor\n"
                "Press Q to quit",
            )
        elif self.state.game_phase == Phase.GAMEPLAY:
            self.phase_display.set_text(
                "Phase: Gameplay\n\nPress ESC to return to main menu",
            )
        elif self.state.game_phase == Phase.EDITOR:
            self.phase_display.set_text(
                "Phase: Editor\n\nPress ESC to return to main menu",
            )
        else:
            pass
        self.phase_display.draw(self.screen)

    def loop(self, fps: int = 60) -> None:  # noqa: C901
        while True:
            for event in pg.event.get():
                if self.state.game_phase == Phase.MAIN_MENU:
                    self.mainmenu.handle_event(event, self.state)
                elif self.state.game_phase == Phase.EXIT:
                    self.exit.handle_event(event, self.state)
                elif self.state.game_phase == Phase.GAMEPLAY:
                    self.gameplay.handle_event(event, self.state)
                elif self.state.game_phase == Phase.EDITOR:
                    self.editor.handle_event(event, self.state)

            if self.state.game_phase == Phase.MAIN_MENU:
                self.mainmenu.update()
                self.mainmenu.draw(self.screen)
            elif self.state.game_phase == Phase.EXIT:
                self.exit.update()
                self.exit.draw(self.screen)
            elif self.state.game_phase == Phase.GAMEPLAY:
                self.gameplay.update()
                self.gameplay.draw(self.screen)
            elif self.state.game_phase == Phase.EDITOR:
                self.editor.update()
                self.editor.draw(self.screen)

            self._update_debug_displays()

            self.state.current_frame += 1
            pg.display.update()
            self.clock.tick(fps)
