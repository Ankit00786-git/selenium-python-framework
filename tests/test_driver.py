from utils.driver_factory import DriverFactory


def test_launch_browser():
    driver = DriverFactory.get_driver()

    driver.get("https://www.google.com")

    print(driver.title)

    assert "Google" in driver.title

    driver.quit()
