import pytest
from datetime import datetime
from pathlib import Path
from utils.driver_factory import DriverFactory
import platform
from utils.screenshot_util import ScreenshotUtil

@pytest.fixture
def driver():
    driver = DriverFactory.get_driver()
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:
            screenshot_dir = Path("screenshots")
            screenshot_dir.mkdir(exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{item.name}_{timestamp}.png"
            filepath = filepath = ScreenshotUtil.capture(
            driver,
            item.name)

            print(f"\nScreenshot captured: {filepath}")

            driver.save_screenshot(str(filepath))

            print(f"\nScreenshot captured: {filepath}")

def pytest_configure(config):
    metadata = config.stash.get("metadata", {})

    metadata["Project"] = "Selenium Python Framework"
    metadata["Framework"] = "PyTest + Selenium"
    metadata["Browser"] = "Chrome"
    metadata["Environment"] = "QA"
    metadata["OS"] = platform.system()
    metadata["Python"] = platform.python_version()

    config.stash["metadata"] = metadata
