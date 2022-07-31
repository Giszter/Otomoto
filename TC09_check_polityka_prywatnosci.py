import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\Hubert\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service=service)


class polityka_prywatnosci(unittest.TestCase):
    def test_polityka_prywatnosci(self):
        driver.get("https://www.otomoto.pl/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
        driver.find_element(By.XPATH, "//a[contains(text(),'Polityka prywatności')]").click()

        assert driver.title == "Polityka prywatności – Centrum Pomocy"
        driver.close()
