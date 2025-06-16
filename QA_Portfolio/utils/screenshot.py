import os
import time
from functools import wraps
from selenium.common.exceptions import WebDriverException


def save_screenshot_on_failure(func):
    @wraps(func)
    def wrapper(driver, *args, **kwargs):
        try:
            return func(driver, *args, **kwargs)
        except Exception as e:
            timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
            screenshot_dir = os.path.join("QA_Portfolio", "screenshots")
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(
                screenshot_dir, f"{func.__name__}_{timestamp}.png")

            try:
                driver.save_screenshot(screenshot_path)
                print(f"📸 Screenshot saved to: {screenshot_path}")
            except WebDriverException as we:
                print(f"⚠️ Failed to capture screenshot: {we}")
            raise e
    return wrapper
