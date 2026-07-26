import logging
from pathlib import Path


class Logger:

    @staticmethod
    def get_logger(name="FrameworkLogger"):

        logger = logging.getLogger(name)

        # Only configure this logger once
        if not logger.handlers:

            logger.setLevel(logging.INFO)

            log_dir = Path("logs")
            log_dir.mkdir(exist_ok=True)

            log_file = log_dir / "framework.log"

            formatter = logging.Formatter(
                "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
            )

            file_handler = logging.FileHandler(log_file, mode="a", encoding="utf-8")
            file_handler.setFormatter(formatter)

            console_handler = logging.StreamHandler()
            console_handler.setFormatter(formatter)

            logger.addHandler(file_handler)
            logger.addHandler(console_handler)

            logger.propagate = False

        return logger
