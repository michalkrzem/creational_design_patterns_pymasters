from abc import abstractmethod, ABC
from typing import List

from config import Configuration


class ConfigFactory(ABC):
    config = Configuration()

    @abstractmethod
    def create_config(self, key):
        pass


class DevelopConfig(ConfigFactory):
    def create_config(self, key: str | int | dict | List) -> Configuration:
        self.config.app_settings["develop"] = key
        return self.config


class ProductionConfig(ConfigFactory):
    def create_config(self, key: str | int | dict | List) -> Configuration:
        self.config.app_settings["production"] = key
        return self.config


class TestConfig(ConfigFactory):
    def create_config(self, key: str | int | dict | List) -> Configuration:
        self.config.app_settings["test"] = key
        return self.config
