from abc import abstractmethod, ABC
from typing import List

from config import Configuration


class ConfigFactory(ABC):
    config = Configuration()

    @abstractmethod
    def set_config(self, value):
        pass


class DevelopConfig(ConfigFactory):
    def set_config(self, value: str | int | dict | List) -> Configuration:
        self.config.app_settings["develop"] = value
        return self.config


class ProductionConfig(ConfigFactory):
    def set_config(self, value: str | int | dict | List) -> Configuration:
        self.config.app_settings["production"] = value
        return self.config


class TestConfig(ConfigFactory):
    def set_config(self, value: str | int | dict | List) -> Configuration:
        self.config.app_settings["test"] = value
        return self.config
