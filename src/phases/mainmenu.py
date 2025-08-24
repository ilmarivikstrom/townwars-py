import pygame as pg
from pygame.locals import K_RETURN, KEYDOWN, QUIT, K_e, K_q

from src.colors import CRUST
from src.config import Config
from src.state import Phase, State
from src.ui.button import Button
from src.utils.logging import setup_logging

logger = setup_logging()

start_button = Button(
    center=(Config.SCREEN_WIDTH / 2, Config.SCREEN_HEIGHT / 2),
    text="Start Game",
)

editor_button = Button(
    center=(Config.SCREEN_WIDTH / 2, Config.SCREEN_HEIGHT / 2 + 50),
    text="Editor",
)

exit_button = Button(
    center=(Config.SCREEN_WIDTH / 2, Config.SCREEN_HEIGHT / 2 + 100),
    text="Exit",
)


def mainmenu_phase(state: State, screen: pg.Surface) -> None:
    screen.fill(CRUST)

    for event in pg.event.get():
        if (event.type == QUIT) or (event.type == KEYDOWN and event.key == K_q):
            state.game_phase = Phase.EXIT
            logger.info("Mainmenu -> Exit.")
            return
        if event.type == KEYDOWN and event.key == K_RETURN:
            state.game_phase = Phase.GAMEPLAY
            logger.info("Mainmenu -> Gameplay.")
            return
        if event.type == KEYDOWN and event.key == K_e:
            state.game_phase = Phase.EDITOR
            logger.info("Mainmenu -> Editor.")
            return

    editor_button.update()
    start_button.update()
    exit_button.update()
    editor_button.draw(screen)
    start_button.draw(screen)
    exit_button.draw(screen)
