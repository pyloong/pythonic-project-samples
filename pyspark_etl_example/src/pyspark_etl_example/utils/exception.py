"""Exception"""


class EtlError(Exception):
    """Etl error"""


class PluginNotFoundError(EtlError):
    """PluginNotFoundError"""

    def __init__(self, namespace: str, name: str):
        super().__init__()
        self._namespace = namespace
        self._name = name

    def __repr__(self):
        return f'Can not found "{self._name}" plugin in {self._namespace}'

    def __str__(self):
        return self.__repr__()
