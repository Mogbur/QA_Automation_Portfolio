import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

from QA_Portfolio.utils.overlay_handler import remove_overlays
from QA_Portfolio.utils.screenshot import save_screenshot_on_failure


def scroll_and_type(driver, by, identifier, value):
    field = driver.find_element(by, identifier)
    driver.execute_script("arguments[0].scrollIntoView(true);", field)
    field.clear()
    field.send_keys(value)


@pytest.mark.usefixtures("driver")
@save_screenshot_on_failure
def test_logout_and_delete_account(driver):
    driver.get("https://automationexercise.com/")
    wait = WebDriverWait(driver, 10)
    print("🌐 Opened homepage.")
    remove_overlays(driver)

    # Step 1: Signup
    login_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Signup / Login")))
    driver.execute_script("arguments[0].click();", login_link)
    print("➡️ Navigated to signup/login page.")
    remove_overlays(driver)

    name_input = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//input[@data-qa='signup-name']")))
    email = f"henri_delete_{int(time.time())}@test.com"
    name_input.send_keys("Henri Delete")
    driver.find_element(
        By.XPATH, "//input[@data-qa='signup-email']").send_keys(email)
    driver.find_element(By.XPATH, "//button[@data-qa='signup-button']").click()
    print("✅ Submitted signup form.")

    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[text()='Enter Account Information']")))
    print("📄 Account info form loaded.")
    remove_overlays(driver)

    # Step 2: Fill account form
    driver.execute_script(
        "arguments[0].click();", driver.find_element(By.ID, "id_gender1"))
    scroll_and_type(driver, By.ID, "password", "TestPassword123")
    Select(driver.find_element(By.ID, "days")).select_by_visible_text("12")
    Select(driver.find_element(By.ID, "months")).select_by_visible_text("June")
    Select(driver.find_element(By.ID, "years")).select_by_visible_text("1990")
    scroll_and_type(driver, By.ID, "first_name", "Henri")
    scroll_and_type(driver, By.ID, "last_name", "QA")
    scroll_and_type(driver, By.ID, "address1", "123 Test St")
    Select(driver.find_element(By.ID, "country")
           ).select_by_visible_text("India")
    scroll_and_type(driver, By.ID, "state", "Turku")
    scroll_and_type(driver, By.ID, "city", "Turku")
    scroll_and_type(driver, By.ID, "zipcode", "20100")
    scroll_and_type(driver, By.ID, "mobile_number", "0401234567")

    driver.find_element(
        By.XPATH, "//button[@data-qa='create-account']").click()
    print("✅ Submitted account info form.")

    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[text()='Account Created!']")))
    print("🎉 Account successfully created.")

    # Step 3: Logout
    continue_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//a[@data-qa='continue-button']")))
    driver.execute_script("arguments[0].click();", continue_btn)
    print("➡️ Clicked continue after account creation.")
    remove_overlays(driver)

    logout_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Logout")))
    driver.execute_script("arguments[0].click();", logout_link)
    print("👋 Logged out.")

    # Step 4: Log back in and delete
    email_input = wait.until(EC.visibility_of_element_located(
        (By.XPATH, "//input[@data-qa='login-email']")))
    remove_overlays(driver)
    driver.execute_script("arguments[0].scrollIntoView(true);", email_input)
    email_input.clear()
    email_input.send_keys(email)

    password_input = driver.find_element(
        By.XPATH, "//input[@data-qa='login-password']")
    password_input.clear()
    password_input.send_keys("TestPassword123")

    driver.find_element(By.XPATH, "//button[@data-qa='login-button']").click()
    print("🔐 Logged back in.")

    delete_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Delete Account")))
    driver.execute_script("arguments[0].click();", delete_link)
    print("💥 Delete Account clicked.")

    wait.until(EC.presence_of_element_located(
        (By.XPATH, "//b[text()='Account Deleted!']")))
    print("✅ Account successfully deleted.")
