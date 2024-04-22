from abc import abstractmethod, ABC
from typing import List

from config import Configuration


class ConfigFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_config(key):
        pass


class DevelopConfig(ConfigFactory, Configuration):
    @staticmethod
    def create_config(key: str | int | dict | List) -> Configuration:
        config = Configuration()
        config.app_settings["develop"] = key
        return config


class ProductionConfig(ConfigFactory, Configuration):
    @staticmethod
    def create_config(key: str | int | dict | List) -> Configuration:
        config = Configuration()
        config.app_settings["production"] = key
        return config


class TestConfig(ConfigFactory, Configuration):
    @staticmethod
    def create_config(key: str | int | dict | List) -> Configuration:
        config = Configuration()
        config.app_settings["test"] = key
        return config
