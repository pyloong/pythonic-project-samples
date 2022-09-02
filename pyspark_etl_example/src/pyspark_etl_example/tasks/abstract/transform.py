from abc import abstractmethod, ABC

from pyspark.sql import DataFrame


class AbstractTransform(ABC):
    """
    Base class to define a DataFrame transformation.
    """

    @abstractmethod
    def transform(self, df: DataFrame) -> DataFrame:
        """Transform original dataset."""
        raise NotImplementedError
