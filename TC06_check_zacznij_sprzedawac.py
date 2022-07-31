import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\Hubert\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service=service)


class zacznij_sprzedawac(unittest.TestCase):
    def test_zacznij_sprzedawac(self):
        driver.get("https://www.otomoto.pl/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
        driver.find_element(By.XPATH, "//button[contains(text(),'Zacznij sprzedawać')]").click()
        create_ad_button = driver.find_element(By.XPATH, "//button[contains(text(),'Stwórz ogłoszenie')]")
        assert create_ad_button.text == "Stwórz ogłoszenie"
        driver.close()
