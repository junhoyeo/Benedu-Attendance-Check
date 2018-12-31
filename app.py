from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json, re

with open('./secret.json', 'r') as f:
    user = json.load(f)

# set options
options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=800x500')
options.add_argument("disable-gpu")

try:
    driver = webdriver.Chrome('./chromedriver', chrome_options=options)
    driver.get('https://benedu.co.kr/Index.aspx')

    # click login button
    driver.find_element_by_css_selector('li#liLogin > a').click()
    driver.implicitly_wait(10)

    # login
    driver.find_element_by_id('inputEmail').send_keys(user['email'])
    driver.find_element_by_id('inputPassword').send_keys(user['password'])
    driver.find_element_by_id('btnLogin').click()
    driver.implicitly_wait(5)

    # get points and rank
    points = driver.find_element_by_id('ucMenuStd_MyPoint_Menu').text
    points = int(points.replace('점', ''))
    rank = driver.find_element_by_id('ucMenuStd_Rank_Menu').text
    rank = int(rank.replace('위', ''))

    driver.quit()
    print(json.dumps({'success': True, 'points': points, 'rank': rank}))

except Exception as e:
    # error
    print(json.dumps({'success': False, 'error': e.message}))
