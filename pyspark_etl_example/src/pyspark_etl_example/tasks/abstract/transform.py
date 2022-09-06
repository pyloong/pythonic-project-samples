"""Base Transform"""
from abc import ABC, abstractmethod

from pyspark.sql import DataFrame


class AbstractTransform(ABC):
    """
    Base class to define a DataFrame transformation.
    """

    @abstractmethod
    def transform(self, df: DataFrame) -> DataFrame:
        """Transform original dataset."""
        raise NotImplementedError
