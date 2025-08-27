from typing import TYPE_CHECKING

import pygame as pg

from src.colors import CRUST
from src.config import Config
from src.state import Phase, State
from src.ui.button import Button
from src.ui.text_display import TextDisplay
from src.utils.logging import setup_logging

if TYPE_CHECKING:
    from src.component import Component

logger = setup_logging()


class MainMenu:
    def __init__(self) -> None:
        self.ui_components: list[Component] = []

        start_button = Button(
            on_click=self._on_start_click,
            center=(Config.SCREEN_WIDTH // 2, Config.SCREEN_HEIGHT // 2),
            text="Start Game",
        )
        editor_button = Button(
            on_click=self._on_editor_click,
            center=(Config.SCREEN_WIDTH // 2, Config.SCREEN_HEIGHT // 2 + 50),
            text="Editor",
        )
        exit_button = Button(
            on_click=self._on_exit_click,
            center=(Config.SCREEN_WIDTH // 2, Config.SCREEN_HEIGHT // 2 + 100),
            text="Exit",
        )
        self.ui_components.append(start_button)
        self.ui_components.append(editor_button)
        self.ui_components.append(exit_button)

        title_text = TextDisplay(
            center=(Config.SCREEN_WIDTH // 2, 200),
            font_size=72,
            padding=10,
            max_width=400,
            background_alpha=0,
            text="TOWNWARS",
        )

        subtitle_text = TextDisplay(
            center=(Config.SCREEN_WIDTH // 2, 240),
            font_size=14,
            padding=10,
            max_width=400,
            background_alpha=0,
            text="Hate your neighbors? Fight them!",
        )
        self.ui_components.append(title_text)
        self.ui_components.append(subtitle_text)

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
        for component in self.ui_components:
            component.handle_event(event)

    def update(self) -> None:
        for component in self.ui_components:
            component.update()

    def draw(self, screen: pg.Surface) -> None:
        screen.fill(CRUST)
        for component in self.ui_components:
            component.draw(screen)
