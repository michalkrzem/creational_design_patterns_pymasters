class Configuration(object):
    _instance = None
    _settings = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Configuration, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self._dicter = {}

    @property
    def dicter(self):
        return self._dicter

    @dicter.setter
    def dicter(self, **kwargs):
        self.dicter.update(kwargs)


a = Configuration()
b = Configuration()

b.dicter["ola"] = "kasia"
print(b.dicter)

a.dicter["kamila"] = "Ewa"
print(a.dicter)


print(id(a))
print(id(b))
print(id(a) == id(b))
