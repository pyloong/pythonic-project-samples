"""Project executor"""
import argparse
import logging

from stevedore import ExtensionManager

from automotive_data_etl.constants import ENV_DEVELOPMENT
from automotive_data_etl.constants import TASK_NAMESPACE
from automotive_data_etl.context import Context
from automotive_data_etl.dependencies.logger import Logger
from automotive_data_etl.executor import Executor


def _parse_args() -> argparse.Namespace:
    """Parameter parsing"""
    parser = argparse.ArgumentParser(allow_abbrev=False)
    # parser add arguments
    parser.add_argument(
        "--env",
        required=False,
        choices=['development', 'testing', 'production'],
        default=ENV_DEVELOPMENT
    )
    parser.add_argument(
        "--task",
        required=True,
        choices=_get_task_list()
    )
    return parser.parse_args()


def _get_task_list():
    """Get task list by namespace"""
    extension_manager = ExtensionManager(namespace=TASK_NAMESPACE, invoke_on_load=False)
    return extension_manager.entry_points_names()


def main() -> None:
    """
    Parse args, init Context, init logger and executor task run.
    """
    args = _parse_args()
    Context().environment = args.env
    ctx = Context()
    logger = Logger(ctx.settings)
    logger.init_log()
    logging.info('etl job init success.')
    logging.info(f'env configs options: {ctx.settings.message}')
    Executor(ctx, args.task).run()


if __name__ == "__main__":
    main()
