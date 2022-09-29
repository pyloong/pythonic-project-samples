"""Base Transform"""
from abc import ABC, abstractmethod

from automotive_data_etl.context import Context


class AbstractTransform(ABC):
    """
    Base class to define a DataFrame transformation.
    """

    # pylint: disable=[too-few-public-methods]

    def __init__(self):
        self.ctx = Context()
        self.settings = self.ctx.settings

    @abstractmethod
    def transform(self, data):
        """Transform original dataset."""
        raise NotImplementedError
