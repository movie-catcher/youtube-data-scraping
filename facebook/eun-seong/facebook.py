import requests
from bs4 import BeautifulSoup
from requests.api import post
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

import env

options = webdriver.ChromeOptions()
# options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")

driver = webdriver.Chrome(env.dirver_path,options=options)
driver.implicitly_wait(3)

url = 'https://www.facebook.com'
filter_year_2020 = 'eyJycF9jcmVhdGlvbl90aW1lOjAiOiJ7XCJuYW1lXCI6XCJjcmVhdGlvbl90aW1lXCIsXCJhcmdzXCI6XCJ7XFxcInN0YXJ0X3llYXJcXFwiOlxcXCIyMDIwXFxcIixcXFwic3RhcnRfbW9udGhcXFwiOlxcXCIyMDIwLTFcXFwiLFxcXCJlbmRfeWVhclxcXCI6XFxcIjIwMjBcXFwiLFxcXCJlbmRfbW9udGhcXFwiOlxcXCIyMDIwLTEyXFxcIixcXFwic3RhcnRfZGF5XFxcIjpcXFwiMjAyMC0xLTFcXFwiLFxcXCJlbmRfZGF5XFxcIjpcXFwiMjAyMC0xMi0zMVxcXCJ9XCJ9IiwicnBfYXV0aG9yOjAiOiJ7XCJuYW1lXCI6XCJtZXJnZWRfcHVibGljX3Bvc3RzXCIsXCJhcmdzXCI6XCJcIn0ifQ%3D%3D'


def login():
    driver.get(url)
    driver.implicitly_wait(10)

    driver.find_element(By.CSS_SELECTOR, 'input[type="text"]#email').send_keys(env.ID)
    driver.find_element(By.CSS_SELECTOR, 'input[type="password"]#pass').send_keys(env.PW)
    driver.find_element(By.CSS_SELECTOR, 'button[name="login"]').click()

def scrollPage():
        while True:
            html = BeautifulSoup(driver.page_source, 'html.parser')
            isFinished = html.find(text='결과 끝')
            if isFinished is not None: break
            # print(isFinished)
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(1)


def get_post_links():
    post_links = []
    html = BeautifulSoup(driver.page_source, 'html.parser')
    for link in html.findAll('a', href=re.compile('^https:\/\/www.facebook.com\/[a-zA-Z0-9]+\/posts\/([0-9]+)$')):
        href = link.attrs['href']
        if href is not None and href not in post_links:
                post_links.append(href)
    return post_links


### main start
try:
    login()
    driver.implicitly_wait(10)
    driver.get('https://www.facebook.com/search/posts/?q=영화%20알라딘&filters='+filter_year_2020)
    scrollPage()    
    links = get_post_links()
    print(links)

except Exception:
    print(Exception)

finally:
    driver.quit()
