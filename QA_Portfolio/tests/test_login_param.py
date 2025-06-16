import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    yield driver
    driver.quit()


@pytest.mark.parametrize("username,password,should_pass", [
    ("tomsmith", "SuperSecretPassword!", True),
    ("tomsmith", "wrongpassword", False),
    ("wronguser", "SuperSecretPassword!", False),
    ("wronguser", "wrongpassword", False)
])
def test_login_param(username, password, should_pass, driver):
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/login")
    wait.until(EC.presence_of_element_located(
        (By.ID, "username"))).send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.CSS_SELECTOR, "button.radius").click()

    flash = wait.until(EC.visibility_of_element_located((By.ID, "flash")))

    if should_pass:
        assert "You logged into a secure area!" in flash.text
    else:
        assert "Your username is invalid!" in flash.text or "Your password is invalid!" in flash.text
