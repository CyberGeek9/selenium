from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
query="Sports"
driver.get(f"https://www.thesun.co.uk/?s={query}")
element = driver.find_elements(By.CLASS_NAME, "text-anchor-wrap")
for elem in element:
    print(elem.text)
# print(elem.get_attribute("outerHTML"))
time.sleep(6)
driver.close()

# ............................................