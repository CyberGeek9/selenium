from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get("https://www.olx.com.pk/vehicles_c5")


containers=driver.find_elements(By.XPATH,'//div[@class="_8b88d490"]')
time.sleep(20)

WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@class="_8b88d490"]'))
)

Models=[]
prices=[]
links=[]

for container in containers:
    try:
      Model=container.find_element(By.XPATH,'.//a').get_attribute("title")
      price = container.find_element(By.XPATH, './/span[contains(@class,"f83175ac")]').text
      link=container.find_element(By.XPATH,'.//a').get_attribute("href")
      prices.append(price)
      Models.append(Model)
      links.append(link)

    except Exception as e:
        print(f"Skipping item due to error: {e}")
        continue

my_dict={'Model':Models,'price':prices,'link':links}

df_Vehicales=pd.DataFrame(my_dict)
df_Vehicales.to_csv('Vehicales.csv')

print("Data saved to Vehicales.csv")


time.sleep(20)
driver.close()