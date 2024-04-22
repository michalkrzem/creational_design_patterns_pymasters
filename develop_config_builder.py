from typing import List

from config_builder import Builder
from config_factory import DevelopConfig


class DevelopConfigBuilder(Builder):
    def __init__(self):
        self.configuration = DevelopConfig()

    def set_database_connection(self, value: str | int | dict | List) -> None:
        self.configuration.app_settings["develop"]["DATABASE"] = value

    def set_env_username(self, value: str | int | dict | List) -> None:
        self.configuration.app_settings["develop"]["ENV_USER"] = value

    def set_host(self, value: str | int | dict | List) -> None:
        self.configuration.app_settings["develop"]["HOST"] = value
