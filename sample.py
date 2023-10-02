from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def fetch_dom_from_url(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    with webdriver.Chrome('/Users/jiachengding/.cache/selenium/chromedriver/mac-arm64/117.0.5938.92/chromedriver', chrome_options=options) as driver:
        driver.get(url)
        try:

            element_present = EC.presence_of_element_located((By.ID, 'element_id'))
            WebDriverWait(driver, 20).until(element_present)
        except Exception as e:
            print(str(e))


        dom_content = driver.execute_script("return document.documentElement.outerHTML;")

    return dom_content

if __name__ == '__main__':
    url = 'https://bugs.chromium.org/p/chromium/issues/detail?id=1292038'
    content = fetch_dom_from_url(url)
    with open(os.path.join(os.path.expanduser('~'), 'Desktop', '1292038.txt'), 'w', encoding='utf-8') as f:
        f.write(content)
