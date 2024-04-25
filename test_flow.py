from config import Configuration
from config_factory import DevelopConfig, ProductionConfig, TestConfig
from develop_config_builder import DevelopConfigBuilder
from production_config_builder import ProductionConfigBuilder

# I create my configuration instances
develop = DevelopConfig()
test = TestConfig()
production = ProductionConfig()
###################################################################################################
# I create configurations by instances: test, prod, dev
test.set_config({
    "DEBUG": None,
    "DATABASE": "MyDatabase"
})
develop.set_config({
    "DEBUG": True,
    "DEFAULT_FROM_EMAIL": "webmaster@example.com"
})
production.set_config({
    "ALLOWED_HOSTS": ["www.example.com"],
    "DEBUG": True,
    "DEFAULT_FROM_EMAIL": "webmaster@example.com"
})
###################################################################################################
# Create global instance of configuration
config_app = Configuration()

# Get special data
print("\nDebug info by develop version:", config_app.app_settings.get("develop").get("DEBUG"))
print("\nAll settings by production version", config_app.app_settings.get("production"))
print("\nSettings for all environments", config_app.app_settings)

###################################################################################################
# Build special configuration by Builder
print("\nPrepare to build special configurations for develop version")
build_develop_config = DevelopConfigBuilder()
print("\nSet database for develop version")
build_develop_config.set_database_connection({
    "PORT": 9999,
    "DATABASE": "PyMasters",
    "USER": "Morpheus",
    "PASSWORD": "hash_hash"
})
print(config_app.app_settings.get("develop"))
print("\nSet special USERNAME variable for develop version")
build_develop_config.set_env_username("MORPHEUS")
print(config_app.app_settings.get("develop").get("ENV_USER"))

###################################################################################################
# Build special configuration by Builder
print("\nPrepare to build special configurations for production version")
build_production_config = ProductionConfigBuilder()
print("\nSet database for production version")
build_production_config.set_database_connection({
    "PORT": 5432,
    "DATABASE": "Postgres",
    "USER": "kvothe",
    "PASSWORD": "hash"
})
print(config_app.app_settings.get("production"))
print("\nSet special USERNAME variable for production version")
build_production_config.set_env_username("NEO")
print(config_app.app_settings.get("production").get("ENV_USER"))
print("\nCheck all settings")
print(config_app.app_settings)

print("\nCheck all settings")
for instance in config_app.app_settings:
    print(f"{instance}: \n{config_app.app_settings.get(instance)}\n")
