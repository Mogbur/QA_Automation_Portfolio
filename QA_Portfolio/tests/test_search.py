import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException,
    NoSuchElementException,
    ElementNotInteractableException,
    ElementClickInterceptedException,
)


@pytest.mark.usefixtures("driver")
def test_search(driver):
    try:
        driver.get("https://automationexercise.com/")
        wait = WebDriverWait(driver, 15)

        # Handle ad iframe popup
        try:
            iframe = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "iframe[src*='google']")))
            driver.switch_to.frame(iframe)
            close_btn = wait.until(
                EC.element_to_be_clickable((By.ID, "dismiss-button")))
            close_btn.click()
            driver.switch_to.default_content()
        except Exception:
            driver.switch_to.default_content()

        # Destroy GDPR/Consent popup (JS nuke or fallback click)
        try:
            overlay = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[role='dialog']")))
            driver.execute_script("arguments[0].remove();", overlay)
            print("💣 Consent popup removed (JS)")
        except:
            try:
                accept_btn = wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[contains(., 'Suuntaa')]"))
                )
                accept_btn.click()
                print("✅ Consent popup removed (Click)")
            except:
                pass

        # Go to Products page
        products_link = wait.until(EC.presence_of_element_located(
            (By.XPATH, "//a[contains(text(), 'Products')]")))
        driver.execute_script(
            "arguments[0].scrollIntoView(true);", products_link)

        try:
            wait.until(EC.element_to_be_clickable(
                (By.XPATH, "//a[contains(text(), 'Products')]")))
            driver.execute_script("arguments[0].click();", products_link)
        except:
            products_link.click()

        # Interact with search box
        search_box = wait.until(
            EC.presence_of_element_located((By.ID, "search_product")))
        try:
            wait.until(EC.element_to_be_clickable((By.ID, "search_product")))
            search_box.clear()
            search_box.send_keys("shirt")
        except ElementNotInteractableException:
            print("⚠️ send_keys failed, using JS fallback.")
            driver.execute_script("arguments[0].value = 'shirt';", search_box)

        # Click search button with bulletproof fallback
        search_btn = wait.until(
            EC.presence_of_element_located((By.ID, "submit_search")))
        try:
            wait.until(EC.element_to_be_clickable((By.ID, "submit_search")))
            search_btn.click()
        except ElementClickInterceptedException:
            print("⚠️ .click() failed, using JS fallback for submit.")
            driver.execute_script("arguments[0].click();", search_btn)

        # Validate search results
        results = wait.until(EC.presence_of_all_elements_located(
            (By.CLASS_NAME, "productinfo")))
        assert len(results) > 0, "No products found in search results!"

    except Exception as e:
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        driver.save_screenshot(f"./screenshots/search_fail_{timestamp}.png")
        raise e
