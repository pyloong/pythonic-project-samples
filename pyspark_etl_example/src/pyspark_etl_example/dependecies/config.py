"""Config Manager"""
from dynaconf import Dynaconf

_settings_files = [
    # All configs file will merge.  # Load default configs.
    'configs/global.toml', 'configs/test.toml', 'configs/prod.toml', 'configs/dev.toml'
]

settings = Dynaconf(
    # Set env `MYPROGRAM='bar'`，use `configs.FOO` .
    envvar_prefix='MYPROGRAM',
    settings_files=_settings_files,
    environments=True,  # multi environments
    load_dotenv=True,  # Enable load .env
    default_env='development',
    lowercase_read=True,
)
