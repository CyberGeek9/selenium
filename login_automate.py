from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")

driver.find_element(By.ID, "username").send_keys("s")
driver.find_element(By.ID, "password").send_keys("P")

driver.find_element(By.CSS_SELECTOR, "button.btn").click()
# Wait for successful login and verify
try:
    # Wait for success element to appear (max 10 seconds)
    success_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h1[contains(text(),'Logged In Successfully')]"))
    )

    # Print success message to console
    print("\n[SUCCESS] Login Successful!")
    print(f"Message displayed on screen: {success_element.text}")

    # JavaScript alert popup
    driver.execute_script("alert('Login Successful! Welcome to the application.');")
    time.sleep(3)  # Let user see the alert

except Exception as e:
    print(f"\n[ERROR] Login failed: {str(e)}")
finally:
    time.sleep(5)
    driver.quit()
