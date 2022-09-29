"""Config Manager"""
from dynaconf import Dynaconf
from dynaconf.base import Settings

__settings_files = [
    # All configs file will merge.  # Load default configs.
    'src/automotive_data_etl/configs/global.toml',
    'src/automotive_data_etl/configs/test.toml',
    'src/automotive_data_etl/configs/prod.toml',
    'src/automotive_data_etl/configs/dev.toml'
]

settings = Dynaconf(
    # Set env `MYPROGRAM='bar'`，use `configs.FOO` .
    envvar_prefix='AUTOMOTIVE_DATA_ETL',
    settings_files=__settings_files,
    environments=True,  # multi environments
    load_dotenv=True,  # Enable load .env
    lowercase_read=True,
)


def overwrite_configs(_settings: Settings, key, value):
    _settings.set(key, value)
