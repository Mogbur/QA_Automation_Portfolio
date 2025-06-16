import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from QA_Portfolio.utils.overlay_handler import remove_overlays
from QA_Portfolio.utils.screenshot import save_screenshot_on_failure


@pytest.mark.usefixtures("driver")
@save_screenshot_on_failure
def test_negative_login_cases(driver):
    driver.get("https://automationexercise.com/")
    wait = WebDriverWait(driver, 10)
    print("🌐 Opened homepage.")

    remove_overlays(driver)

    # Navigate to login page
    login_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Signup / Login")))
    driver.execute_script("arguments[0].click();", login_link)
    print("➡️ Navigated to login page.")
    remove_overlays(driver)

    login_section = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "login-form")))
    driver.execute_script("arguments[0].scrollIntoView(true);", login_section)

    invalid_cases = [
        {"email": "valid@example.com", "password": "wrongpass"},
        {"email": "", "password": "nopass"},
        {"email": "valid@example.com", "password": ""},
        {"email": "not-an-email", "password": "123456"},
    ]

    for i, creds in enumerate(invalid_cases, 1):
        try:
            print(f"🧪 Case {i}: Testing with {creds}")

            # 🛡️ Call this before interacting each time
            remove_overlays(driver)

            email_input = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@data-qa='login-email']")))
            password_input = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//input[@data-qa='login-password']")))

            email_input.clear()
            password_input.clear()

            email_input.click()
            email_input.send_keys(creds["email"])
            password_input.send_keys(creds["password"])

            login_button = wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//button[@data-qa='login-button']")))
            login_button.click()

            error_elem = wait.until(EC.visibility_of_element_located(
                (By.XPATH, "//p[contains(text(),'incorrect')]")))
            assert error_elem.is_displayed()
            print("✅ Error message displayed correctly:", error_elem.text)

        except Exception as e:
            print(f"❌ Error in case {i}:", str(e))
            raise e
