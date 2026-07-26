from pathlib import Path
from datetime import datetime


class ScreenshotUtil:

    @staticmethod
    def capture(driver, name="Screenshot"):
        """
        Capture and save a screenshot.
        Returns the screenshot path.
        """

        screenshot_dir = Path("screenshots")
        screenshot_dir.mkdir(exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

        filename = f"{name}_{timestamp}.png"

        filepath = screenshot_dir / filename

        driver.save_screenshot(str(filepath))

        return str(filepath)
