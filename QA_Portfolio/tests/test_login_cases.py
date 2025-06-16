import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Reusable login helper


def perform_login(username, password):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")
    wait = WebDriverWait(driver, 10)

    wait.until(EC.presence_of_element_located(
        (By.ID, "username"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    return driver, wait

# ✅ SUCCESS test


def test_login_success():
    driver, wait = perform_login("tomsmith", "SuperSecretPassword!")
    message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    assert "You logged into a secure area!" in message.text
    driver.quit()

# ❌ FAILURE test


def test_login_failure():
    driver, wait = perform_login("wronguser", "wrongpassword")
    message = wait.until(EC.visibility_of_element_located((By.ID, "flash")))
    assert "Your username is invalid!" in message.text
    driver.quit()
