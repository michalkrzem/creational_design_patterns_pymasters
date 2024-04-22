from abc import ABC, abstractmethod
from typing import List


class Builder(ABC):
    @abstractmethod
    def set_database_connection(self, value: str | int | dict | List) -> None:
        pass

    @abstractmethod
    def set_env_username(self, value: str | int | dict | List) -> None:
        pass

    @abstractmethod
    def set_host(self, value: str | int | dict | List) -> None:
        pass
