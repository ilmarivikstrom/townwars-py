from src.phases.phase import Phase
from src.utils.logging import setup_logging

logger = setup_logging()


class State:
    def __init__(self) -> None:
        self.game_phase: Phase = Phase.MAIN_MENU
        self.current_frame: int = 0
        logger.info("State initialized. Currently in Mainmenu phase.")
