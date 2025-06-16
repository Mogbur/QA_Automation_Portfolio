import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from QA_Portfolio.utils.screenshot import save_screenshot_on_failure
from QA_Portfolio.utils.overlay_handler import remove_overlays


@pytest.mark.usefixtures("driver")
@save_screenshot_on_failure
def test_search_intentional_fail(driver):
    driver.get("https://automationexercise.com/")
    wait = WebDriverWait(driver, 10)
    print("🌐 Opened homepage.")

    remove_overlays(driver)

    try:
        search_input = wait.until(
            EC.element_to_be_clickable((By.ID, "search_product")))
        remove_overlays(driver)
        search_input.send_keys("nonexistentproduct12345")

        search_button = driver.find_element(By.ID, "submit_search")
        driver.execute_script("arguments[0].click();", search_button)
        print("🔍 Performed fake product search.")
    except Exception as e:
        print(f"⚠️ Could not interact with search input: {e}")
        raise

    # Wait for "No products found" or similar — intentionally fail
    wait.until(EC.presence_of_element_located(
        (By.ID, "search_product")))  # Dummy wait
    print("❌ Now forcing a fake assertion to trigger screenshot.")
    assert False, "Intentional failure to demo screenshot & error capture."
