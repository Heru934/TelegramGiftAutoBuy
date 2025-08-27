import datetime
import logging
import sys


class TimestampFormatter(logging.Formatter):
    def __init__(self):
        super().__init__('%(message)s')

    def format(self, record):
        timestamp = datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S")
        record.message = f"[{timestamp}] - [{record.levelname}]: {record.getMessage()}"
        return record.message


logger = logging.getLogger("gifts_buyer")
logger.setLevel(logging.DEBUG)

handler = logging.StreamHandler(sys.stdout)
handler.setLevel(logging.DEBUG)
handler.setFormatter(TimestampFormatter())
logger.addHandler(handler)


class LoggerInterface:
    @staticmethod
    def _log_clear(level_method, message: str) -> None:
        print("\r", end="")
        level_method(message)

    @staticmethod
    def info(message: str) -> None:
        LoggerInterface._log_clear(logger.info, message)

    @staticmethod
    def warn(message: str) -> None:
        LoggerInterface._log_clear(logger.warning, message)

    @staticmethod
    def error(message: str) -> None:
        LoggerInterface._log_clear(logger.error, message)

    @staticmethod
    def log_same_line(message: str, level: str = "INFO") -> None:
        timestamp = datetime.datetime.now().strftime("%d.%m.%y %H:%M:%S")
        print(f"\r[{timestamp}] - [{level.upper()}]: {message}", end="", flush=True)


info = LoggerInterface.info
warn = LoggerInterface.warn
error = LoggerInterface.error
log_same_line = LoggerInterface.log_same_line
