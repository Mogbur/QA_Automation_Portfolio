import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from QA_Portfolio.utils.overlay_handler import remove_overlays
from QA_Portfolio.utils.screenshot import save_screenshot_on_failure


@pytest.mark.usefixtures("driver")
@save_screenshot_on_failure
def test_account_creation_fill_form(driver):
    driver.get("https://automationexercise.com/")
    wait = WebDriverWait(driver, 10)
    print("🌐 Opened homepage.")

    remove_overlays(driver)

    # Go to Signup/Login
    login_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Signup / Login")))
    driver.execute_script("arguments[0].click();", login_link)
    print("➡️ Navigated to signup/login page.")
    remove_overlays(driver)

    # Fill Signup Form
    name_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@data-qa='signup-name']")))
    email_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@data-qa='signup-email']")))

    remove_overlays(driver)  # <- crucial to avoid interaction issues

    name_input.send_keys("Henri QA3")
    email_input.send_keys(f"henri_qa3_{int(time.time())}@test.com")

    signup_button = driver.find_element(
        By.XPATH, "//button[@data-qa='signup-button']")
    driver.execute_script("arguments[0].click();", signup_button)
    print("✅ Signup form submitted.")

    # Verify confirmation
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[text()='Enter Account Information']")))
    print("🎉 Account successfully created.")
