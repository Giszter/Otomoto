import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\Hubert\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service=service)


class ustawienia_cookie(unittest.TestCase):
    def test_ustawienia_cookie(self):
        driver.get("https://www.otomoto.pl/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Ustawienia plików cookie']").click()
        settings_window = driver.find_element(By.XPATH, "//h2[@id='ot-pc-title']")
        settings_window.is_displayed()
        assert settings_window.text == "Twoja prywatność"
        driver.close()
