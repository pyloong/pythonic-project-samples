"""Base Task"""
from abc import ABC, abstractmethod

from automotive_data_etl.context import Context


class AbstractTask(ABC):
    """
    Base class to read a dataset, transform it, and save it to a table.
    """

    # pylint: disable=[too-few-public-methods]

    def __init__(self):
        self.ctx = Context()
        self.settings = self.ctx.settings

    def run(self) -> None:
        """Execute task module"""
        data = self._extract()
        data_transformed = self._transform(data)
        self._load(data_transformed)

    @abstractmethod
    def _extract(self):
        """extract tmp from file/database/other."""
        raise NotImplementedError

    @abstractmethod
    def _transform(self, data):
        """Transform incoming tmp, and output the transform result"""
        raise NotImplementedError

    @abstractmethod
    def _load(self, data) -> None:
        """Load tmp to file/database/other."""
        raise NotImplementedError
