import functools
import logging
from logging.handlers import RotatingFileHandler

_log_format = '%(asctime)s, %(levelname)s, %(name)s, %(message)s'


def get_file_handler():
    file_handler = RotatingFileHandler(
        "logfile.log",
        maxBytes=10**6,
        backupCount=5,
        encoding="UTF-8"
    )
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(logging.Formatter(_log_format))
    return file_handler


def get_stream_handler():
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(logging.INFO)
    stream_handler.setFormatter(logging.Formatter(_log_format))
    return stream_handler


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)
    logger.addHandler(get_file_handler())
    logger.addHandler(get_stream_handler())
    return logger


logger = get_logger(__name__)


def log(text):
    def _log(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                logger.info(text)
                return result
            except Exception as e:
                err_text = f"Ошибка в {func.__name__}. Ошибка: {str(e)} \n"
                if args:
                    err_text = (f"Такие аргументы привели к ошибке {args}. "
                                + err_text)
                logger.warning(err_text)
                raise e
        return wrapper
    return _log
