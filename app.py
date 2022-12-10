import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

path = os.environ["DRIVER_PATH"]

driver = webdriver.Chrome(path)
driver.get('https://www.warhammer-community.com/latest-news-features/')
driver.implicitly_wait(5)
button = driver.find_element(By.ID, 'onetrust-accept-btn-handler')
button.click()
html = driver.find_element(By.ID, 'articles').get_attribute('innerHTML').replace('\n', '').split('href="')
html.pop(0)
driver.close()
articles = list()
for i in html:
    articles.append(i.split('"')[0])

print(articles)
