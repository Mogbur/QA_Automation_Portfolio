from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")

wait = WebDriverWait(driver, 10)

# Accept cookies if they exist
try:
    accept_btn = wait.until(EC.element_to_be_clickable(
        (By.XPATH, "//div[contains(@class, 'VfPpkd-RLmnJb') or @id='L2AGLb']")))
    accept_btn.click()
    print("✅ Accepted cookies")
except:
    print("⚠️ No cookie popup appeared")

# Use JavaScript to fill and submit the search
try:
    js_script = """
        const box = document.getElementsByName('q')[0];
        box.value = 'OpenAI ChatGPT';
        const form = box.form;
        form.submit();
    """
    driver.execute_script(js_script)
    print("✅ Search injected via JS")
except Exception as e:
    print("❌ JS injection failed:", e)

# Wait and take screenshot
time.sleep(3)
driver.save_screenshot("search_result.png")
driver.quit()

# This script automates a Google search for "OpenAI ChatGPT" and saves a screenshot of the results.
# Ensure you have the necessary packages installed:
# pip install selenium webdriver-manager
