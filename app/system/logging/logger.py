import logging
import sys


def setup_logger() -> logging.Logger:
    logger = logging.getLogger("py-core")
    logger.setLevel(logging.INFO)

    # Prevent duplicate handlers in reload
    if logger.handlers:
        return logger

    handler = logging.StreamHandler(sys.stdout)
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False
    return logger
