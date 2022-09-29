"""Logger"""
import os
import logging
from logging.config import dictConfig

from dynaconf.base import Settings

from automotive_data_etl.constants import DEFAULT_ENCODING


class Logger:
    """
    This is Logger config class, you can init logger config for logging.
    param ctx_settings: Context() settings
    """

    def __init__(self, ctx_settings: Settings):
        self.settings = ctx_settings
        self.log_path = self.get_log_path()

    def get_log_path(self):
        """
        Get or Create default log path
        Default log path: "../../{project root path}/log/all.log"
        """
        if not self.settings.LOGPATH or not self.settings.exists('logpath'):
            root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            root_path = os.path.abspath(os.path.join(root_path, "../.."))
            log_path = os.path.join(root_path, 'log')
            os.makedirs(log_path, exist_ok=True)
            return log_path
        log_path = self.settings.LOGPATH
        if not os.path.exists(log_path):
            raise FileNotFoundError(f'Can not found directory: "{log_path}" ')
        return log_path

    @staticmethod
    def verbose_formatter(verbose: int) -> str:
        """formatter factory"""
        if verbose is True:
            return 'verbose'
        return 'simple'

    def update_log_level(self, debug: bool, level: str) -> str:
        """update log level"""
        if debug is True:
            level_num = logging.DEBUG
        else:
            level_num = logging.getLevelName(level)
        self.settings.set('LOGLEVEL', logging.getLevelName(level_num))
        return self.settings.LOGLEVEL

    def init_log(self) -> None:
        """Init log config."""
        log_level = self.update_log_level(self.settings.DEBUG, str(self.settings.LOGLEVEL).upper())

        log_config = {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                'verbose': {
                    'format': '%(asctime)s %(levelname)s %(name)s %(process)d %(thread)d %(message)s',
                },
                'simple': {
                    'format': '%(asctime)s %(levelname)s %(name)s %(message)s',
                },
            },
            "handlers": {
                "console": {
                    "formatter": self.verbose_formatter(self.settings.VERBOSE),
                    'level': 'DEBUG',
                    "class": "logging.StreamHandler",
                },
                'file': {
                    'class': 'logging.handlers.RotatingFileHandler',
                    'level': 'DEBUG',
                    'formatter': self.verbose_formatter(self.settings.VERBOSE),
                    'filename': os.path.join(self.log_path, 'all.log'),
                    'maxBytes': 1024 * 1024 * 1024 * 200,  # 200M
                    'backupCount': '5',
                    'encoding': DEFAULT_ENCODING
                },
            },
            "loggers": {
                '': {'level': log_level, 'handlers': ['console']},
            }
        }

        dictConfig(log_config)
