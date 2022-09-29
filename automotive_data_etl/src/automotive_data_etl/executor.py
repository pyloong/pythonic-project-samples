"""
Loads a Task class and calls its `run()` method.
"""
import logging
from typing import Callable

from stevedore import ExtensionManager

from automotive_data_etl.constants import TASK_NAMESPACE
from automotive_data_etl.context import Context
from automotive_data_etl.utils.exception import PluginNotFoundError


class Executor:
    """
    Loads a Task class and calls its `run()` method.
    """
    # pylint: disable=too-few-public-methods

    def __init__(self, ctx: Context, task: str):
        self.ctx = ctx
        self.task = task

    def run(self) -> None:
        """calls its `run()` method in the task class"""
        task_class = self._load_task(TASK_NAMESPACE, self.task)
        logging.info(f"Running task: {task_class}")
        task_class(self.ctx).run()

    @staticmethod
    def _load_task(namespace: str, name: str) -> Callable:
        """Get extension by name from namespace, return task obj"""
        extension_manager = ExtensionManager(namespace=namespace, invoke_on_load=False)
        for ext in extension_manager.extensions:
            if ext.name == name:
                return ext.plugin
            logging.warning(f'Load plugin: {ext.plugin} in namespace "{namespace}"')
        raise PluginNotFoundError(namespace=namespace, name=name)
