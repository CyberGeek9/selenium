from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pandas as pd
import time
driver = webdriver.Chrome()

driver.get("https://www.npr.org/sections/world/")
containers = driver.find_elements(By.XPATH, '//div[@class="item-info"]')

titles=[]
subtitles =[]
links=[]

for container in containers:
      title=container.find_element(By.XPATH,'./h2').text
      subtitle=container.find_element(By.XPATH,'./p').text
      link=container.find_element(By.XPATH,'.//a').get_attribute("href")
      titles.append(title)
      subtitles.append(subtitle)
      links.append(link)

my_dict={'title':titles,'subtitle':subtitles,'link':links}

df_headlines=pd.DataFrame(my_dict)
df_headlines.to_csv('headlines.csv')



time.sleep(10)
driver.close()