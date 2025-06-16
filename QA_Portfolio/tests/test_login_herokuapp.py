import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("driver")
def test_login_herokuapp(driver):
    try:
        driver.get("https://the-internet.herokuapp.com/login")
        wait = WebDriverWait(driver, 10)
        print("🌐 Opened HerokuApp Login Page")

        # Fill credentials
        username_input = wait.until(
            EC.presence_of_element_located((By.ID, "username")))
        username_input.send_keys("tomsmith")

        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("SuperSecretPassword!")

        login_button = driver.find_element(By.CSS_SELECTOR, "button.radius")
        login_button.click()
        print("🔐 Submitted login form")

        # Check success
        message = wait.until(
            EC.visibility_of_element_located((By.ID, "flash")))
        assert "You logged into a secure area!" in message.text
        print("✅ Login successful")

    except Exception as e:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        driver.save_screenshot(f"./screenshots/login_fail_{timestamp}.png")
        print(f"❌ Login test failed: {e}")
        raise
