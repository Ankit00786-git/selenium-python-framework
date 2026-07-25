from config.config_reader import ConfigReader


def test_config_reader():

    print("Browser :", ConfigReader.get_browser())

    print("Headless :", ConfigReader.get_headless())

    print("Base URL :", ConfigReader.get_base_url())

    print("Implicit Wait :", ConfigReader.get_implicit_wait())

    assert ConfigReader.get_browser() == "chrome"
