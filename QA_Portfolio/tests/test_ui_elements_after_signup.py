import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from QA_Portfolio.utils.screenshot import save_screenshot_on_failure
from QA_Portfolio.utils.overlay_handler import remove_overlays


@pytest.mark.usefixtures("driver")
@save_screenshot_on_failure
def test_ui_elements_after_signup(driver):
    driver.get("https://automationexercise.com/")
    wait = WebDriverWait(driver, 10)
    print("🌐 Opened homepage.")

    remove_overlays(driver)

    # Go to signup/login page
    login_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Signup / Login")))
    driver.execute_script("arguments[0].click();", login_link)
    print("➡️ Navigated to signup/login page.")
    remove_overlays(driver)

    # Fill signup form
    name_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@data-qa='signup-name']")))
    email_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@data-qa='signup-email']")))
    name_input.send_keys("Henri UI")
    email_input.send_keys(f"henri_ui_{int(time.time())}@test.com")

    signup_button = driver.find_element(
        By.XPATH, "//button[@data-qa='signup-button']")
    driver.execute_script("arguments[0].click();", signup_button)
    print("✅ Signup form submitted.")

    # Confirm that the next page loaded
    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[text()='Enter Account Information']")))
    print("🎉 Signup success page loaded.")

    # Just check for a couple of UI elements visible on the page
    title_label = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//label[@for='id_gender1']")))
    assert title_label.is_displayed(), "❌ Title (Mr.) radio not visible"

    name_field = wait.until(EC.visibility_of_element_located((By.ID, "name")))
    assert name_field.is_displayed(), "❌ Name field not visible"

    email_field = wait.until(
        EC.visibility_of_element_located((By.ID, "email")))
    assert email_field.is_displayed(), "❌ Email field not visible"

    print("✅ All critical UI elements are visible post-signup.")
