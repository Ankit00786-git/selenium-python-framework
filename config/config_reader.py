import configparser
from pathlib import Path


class ConfigReader:
    """
    Reads values from config/config.ini
    """

    _config = configparser.ConfigParser()

    config_path = Path(__file__).parent / "config.ini"

    _config.read(config_path)

    @classmethod
    def get_browser(cls):
        return cls._config["DEFAULT"]["browser"]

    @classmethod
    def get_headless(cls):
        return cls._config.getboolean("DEFAULT", "headless")

    @classmethod
    def get_base_url(cls):
        return cls._config["DEFAULT"]["base_url"]

    @classmethod
    def get_implicit_wait(cls):
        return cls._config.getint("DEFAULT", "implicit_wait")

    @classmethod
    def get_page_load_timeout(cls):
        return cls._config.getint("DEFAULT", "page_load_timeout")
