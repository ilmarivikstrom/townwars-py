import pygame as pg

from src.colors import CRUST
from src.config import Config
from src.state import Phase, State
from src.ui.button import Button
from src.utils.logging import setup_logging

logger = setup_logging()


class MainMenu:
    def __init__(self) -> None:
        self.components = []

        start_button = Button(
            on_click=self._on_start_click,
            center=(Config.SCREEN_WIDTH / 2, Config.SCREEN_HEIGHT / 2),
            text="Start Game",
        )
        editor_button = Button(
            on_click=self._on_editor_click,
            center=(Config.SCREEN_WIDTH / 2, Config.SCREEN_HEIGHT / 2 + 50),
            text="Editor",
        )
        exit_button = Button(
            on_click=self._on_exit_click,
            center=(Config.SCREEN_WIDTH / 2, Config.SCREEN_HEIGHT / 2 + 100),
            text="Exit",
        )
        self.components.append(start_button)
        self.components.append(editor_button)
        self.components.append(exit_button)

    def _on_start_click(self) -> None:
        logger.info("Mainmenu -> Gameplay.")
        self.state.game_phase = Phase.GAMEPLAY

    def _on_editor_click(self) -> None:
        logger.info("Mainmenu -> Editor.")
        self.state.game_phase = Phase.EDITOR

    def _on_exit_click(self) -> None:
        logger.info("Mainmenu -> Exit.")
        self.state.game_phase = Phase.EXIT

    def handle_event(self, event: pg.event.Event, state: State) -> None:
        self.state = state
        if (event.type == pg.QUIT) or (
            event.type == pg.KEYDOWN and event.key == pg.K_q
        ):
            logger.info("Mainmenu -> Exit.")
            state.game_phase = Phase.EXIT
            return
        if event.type == pg.KEYDOWN and event.key == pg.K_RETURN:
            logger.info("Mainmenu -> Gameplay.")
            state.game_phase = Phase.GAMEPLAY
            return
        if event.type == pg.KEYDOWN and event.key == pg.K_e:
            logger.info("Mainmenu -> Editor.")
            state.game_phase = Phase.EDITOR
            return
        for component in self.components:
            component.handle_event(event)

    def update(self) -> None:
        for component in self.components:
            component.update()

    def draw(self, screen: pg.Surface) -> None:
        screen.fill(CRUST)
        for component in self.components:
            component.draw(screen)
