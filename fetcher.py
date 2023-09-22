from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BugFetcher:

    def __init__(self):
        self.driver = webdriver.Chrome()

    def fetch_ids(self, url):
        self.driver.get(url)
        try:
            wait = WebDriverWait(self.driver, 30)
            wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(@class, 'id')]/a")))

            id_elements = self.driver.find_elements(By.XPATH, "//td[contains(@class, 'id')]/a")
            ids = [elem.text for elem in id_elements]
            return ids
        except Exception as e:
            print("Error occurred:", str(e))
            return []

    def close(self):
        self.driver.close()


if __name__ == '__main__':
    url = "https://bugs.chromium.org/p/chromium/issues/list"
    fetcher = BugFetcher()
    ids = fetcher.fetch_ids(url)
    print(ids)
    # fetcher.close()  see the browser status

