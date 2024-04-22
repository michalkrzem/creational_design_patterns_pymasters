from abc import ABC, abstractmethod


class Configuration:
    _instance = None
    _app_settings = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
        return cls._instance

    @property
    def app_settings(self):
        return self._app_settings

    @app_settings.setter
    def app_settings(self, **kwargs):
        self._app_settings.update(kwargs)


class ConfigFactory(ABC):
    @staticmethod
    @abstractmethod
    def create_config(key):
        pass

    @abstractmethod
    def set_database_connection(self, value):
        pass


class DevelopConfig(ConfigFactory, Configuration):
    @staticmethod
    def create_config(key):
        config = Configuration()
        config.app_settings["develop"] = key
        return config

    def set_database_connection(self, value):
        self.app_settings["develop"]["database"] = value


class ProductionConfig(ConfigFactory, Configuration):
    @staticmethod
    def create_config(key):
        config = Configuration()
        config.app_settings["production"] = key
        return config

    def set_database_connection(self):
        pass


class TestConfig(ConfigFactory, Configuration):
    @staticmethod
    def create_config(key):
        config = Configuration()
        config.app_settings["test"] = key
        return config

    def set_database_connection(self):
        pass


develop = DevelopConfig()
production = ProductionConfig()
test = TestConfig()

develop.create_config({"Debug": True, "database": "Postgres"})
production.create_config({"Debug": False, "database": "SQLite"})
test.create_config({"Debug": None, "database": "MyDatabase"})

develop.set_database_connection({"PORT": 5432, "DATABASE": "Postgres"})

print(develop.app_settings.get("develop").get("Debug"))
print(production.app_settings.get("production"))
print(test.app_settings)
