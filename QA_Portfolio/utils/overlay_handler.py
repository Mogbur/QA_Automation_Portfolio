from selenium.webdriver.common.by import By


def remove_overlays(driver):
    overlay_selectors = ["div[class*='fc-dialog']",
                         "div[class*='consent']", "div[class*='overlay']"]
    for selector in overlay_selectors:
        try:
            overlays = driver.find_elements(By.CSS_SELECTOR, selector)
            for overlay in overlays:
                driver.execute_script("arguments[0].remove();", overlay)
                print(f"🔥 Removed overlay: {selector}")
        except Exception:
            print(f"⚠️ Overlay not found or stale: {selector}")
