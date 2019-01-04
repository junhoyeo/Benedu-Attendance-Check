"""Benedu Attendance Check"""

import json
import logging
import os.path
from selenium import webdriver

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

def auto_check(user):
    """Auto Benedu Attendance Check with user credentials"""

    # set options
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=800x500')
    options.add_argument("disable-gpu")

    try:
        driver_path = os.path.join(CURRENT_DIR, './chromedriver')
        driver = webdriver.Chrome(driver_path, chrome_options=options)
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
        return {'success': True, 'points': points, 'rank': rank}

    except Exception as err:
        # error
        logging.exception(err)
        return {'success': False, 'error': str(err)}

def main():
    """Dedicated main function"""

    with open(os.path.join(CURRENT_DIR, './secret.json'), 'r') as file:
        user = json.load(file)
    result = auto_check(user)
    print(json.dumps(result))

if __name__ == '__main__':
    main()
