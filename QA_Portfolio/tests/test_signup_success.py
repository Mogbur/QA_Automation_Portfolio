from QA_Portfolio.utils.overlay_handler import remove_overlays
from QA_Portfolio.utils.screenshot import save_screenshot_on_failure
import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os


@pytest.mark.usefixtures("driver")
@save_screenshot_on_failure
def test_signup_success(driver):
    driver.get("https://automationexercise.com/")
    wait = WebDriverWait(driver, 10)
    print("🌐 Opened homepage.")

    remove_overlays(driver)

    login_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Signup / Login")))
    driver.execute_script("arguments[0].click();", login_link)
    print("➡️ Navigated to signup/login page.")
    remove_overlays(driver)

    name_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@data-qa='signup-name']")))
    email_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@data-qa='signup-email']")))
    name_input.clear()
    email_input.clear()
    name_input.send_keys("Henri QA")
    email_input.send_keys(f"henri_qa_{int(time.time())}@test.com")

    signup_button = driver.find_element(
        By.XPATH, "//button[@data-qa='signup-button']")
    driver.execute_script("arguments[0].click();", signup_button)
    print("✅ Submitted signup form.")

    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[text()='Enter Account Information']")))
    print("🎉 Signup success reached.")
