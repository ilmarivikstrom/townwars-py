import logging

from src.config import Config


def setup_logging(log_level: str = Config.LOG_LEVEL) -> logging.Logger:
    fmt = "%(asctime)s %(funcName)10s(): %(message)s"
    logging.basicConfig(level=log_level, format=fmt)
    return logging.getLogger()
