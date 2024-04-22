from typing import List

from config_builder import Builder
from config_factory import ProductionConfig


class ProductionConfigBuilder(Builder):
    def __init__(self):
        self.configuration = ProductionConfig()

    def set_database_connection(self, value: str | int | dict | List):
        self.configuration.app_settings["production"]["DATABASE"] = value

    def set_env_username(self, value: str | int | dict | List):
        self.configuration.app_settings["production"]["ENV_USER"] = value

    def set_host(self, value: str | int | dict | List):
        self.configuration.app_settings["production"]["HOST"] = value
