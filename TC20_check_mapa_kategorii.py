import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\Hubert\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service=service)


class mapa_kategorii(unittest.TestCase):
    def test_mapa_kategorii(self):
        driver.get("https://www.otomoto.pl/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Mapa kategorii']").click()
        mapa_kategorii_text = driver.find_element(By.XPATH, "//h1[normalize-space()='Mapa kategorii']")
        assert mapa_kategorii_text.text == "Mapa kategorii"
        driver.close()
