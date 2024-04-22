class Configuration:
    _instance = None
    _app_settings = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
        return cls._instance

    @property
    def app_settings(self) -> dict:
        return self._app_settings

    @app_settings.setter
    def app_settings(self, **kwargs) -> None:
        self._app_settings.update(kwargs)
