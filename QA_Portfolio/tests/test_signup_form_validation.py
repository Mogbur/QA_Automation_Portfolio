import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-popup-blocking")
    driver = webdriver.Chrome(service=Service(
        ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def remove_overlays(driver):
    overlay_selectors = [
        "div[class*='fc-dialog']",
        "div[class*='overlay']",
        "div[class*='consent']",
        "div[id*='cookie']",
        "div[class*='popup']"
    ]
    for selector in overlay_selectors:
        try:
            driver.execute_script("""
                let el = document.querySelector(arguments[0]);
                if (el) { el.remove(); console.log('🔥 Removed overlay:', arguments[0]); }
            """, selector)
        except Exception:
            print(f"⚠️ Overlay not found or stale: {selector}")


def test_signup_form_validation(driver):
    driver.get("https://automationexercise.com/")
    wait = WebDriverWait(driver, 10)
    print("🌐 Opened homepage.")

    time.sleep(2)
    remove_overlays(driver)

    # Click Signup/Login
    login_link = wait.until(EC.element_to_be_clickable(
        (By.LINK_TEXT, "Signup / Login")))
    driver.execute_script("arguments[0].click();", login_link)
    print("➡️ Navigated to signup page.")
    time.sleep(2)

    # Scroll to form and remove overlays again
    form_section = wait.until(
        EC.visibility_of_element_located((By.CLASS_NAME, "signup-form")))
    driver.execute_script("arguments[0].scrollIntoView(true);", form_section)
    time.sleep(1)
    remove_overlays(driver)

    try:
        name_input = wait.until(
            EC.visibility_of_element_located((By.NAME, "name")))
        email_input = wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//input[@data-qa='signup-email']")))

        driver.execute_script("arguments[0].scrollIntoView(true);", name_input)
        name_input.clear()
        name_input.send_keys("TestUser")

        driver.execute_script(
            "arguments[0].scrollIntoView(true);", email_input)
        email_input.clear()
        email_input.send_keys("invalidemail")
        print("✍️ Filled invalid signup data.")
    except Exception as e:
        print(f"❌ Failed to fill signup fields: {e}")
        raise

    try:
        signup_btn = wait.until(EC.element_to_be_clickable(
            (By.XPATH, "//button[@data-qa='signup-button']")))
        driver.execute_script("arguments[0].click();", signup_btn)
        print("📨 Submitted signup form.")
    except Exception as e:
        print(f"❌ Signup button issue: {e}")
        raise

    try:
        # Check if the email input field is invalid
        is_invalid = driver.execute_script("""
                return arguments[0].validity.valid === false;
            """, email_input)
        assert is_invalid, "❌ Email field was unexpectedly valid!"
        print("✅ Email validation triggered correctly (HTML5).")
    except Exception as e:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        driver.save_screenshot(
            f"./screenshots/test_signup_form_validation_{timestamp}.png")
        print(f"❌ Validation failed: {e}")
        raise
