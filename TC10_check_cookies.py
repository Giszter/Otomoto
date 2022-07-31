import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\Hubert\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service=service)


class cookies(unittest.TestCase):
    def test_cookies(self):
        driver.get("https://www.otomoto.pl/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
        driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > "
                                             "div:nth-child(2) > footer:nth-child(3) > section:nth-child(1) > "
                                             "article:nth-child(2) > ul:nth-child(2) > li:nth-child(7) > p:nth-child("
                                             "1) > a:nth-child(1)").click()

        assert driver.title == "Polityka Plików Cookies i Podobnych Technologii – Centrum Pomocy"
        driver.close()
