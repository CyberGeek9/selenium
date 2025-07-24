from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time

driver = webdriver.Chrome()
query="mobile"
driver.get(f"https://www.daraz.pk/catalog/?spm=a2a0e.tm80335142.search.d_go&q={query}")

WebDriverWait(driver, 15).until(
    EC.presence_of_all_elements_located((By.XPATH, '//div[@class="buTCk"]'))
)

containers=driver.find_elements(By.XPATH,'//div[@class="buTCk"]')
time.sleep(10)

titles=[]
prices=[]
links=[]

for container in containers:
    try:
      title=container.find_element(By.XPATH,'.//a').text
      price=container.find_element(By.XPATH,'.//span[contains(@class,"ooOxS")]').text
      link=container.find_element(By.XPATH,'.//a').get_attribute("href")
      titles.append(title)
      prices.append(price)
      links.append(link)

    except Exception as e:
        print(f"Skipping item due to error: {e}")
        continue

my_dict={'title':titles,'price':prices,'link':links}

df_TotalStock=pd.DataFrame(my_dict)
df_TotalStock.to_csv('TotalStock.csv')

print("Data saved to TotalStock.csv")
time.sleep(15)
driver.close()




