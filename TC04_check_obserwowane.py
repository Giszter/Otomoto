import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\Hubert\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service=service)


class obserwowane(unittest.TestCase):
    def test_obserwowane(self):
        driver.get("https://www.otomoto.pl/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
        driver.find_element(By.XPATH, "//span[normalize-space()='Obserwowane']").click()
        twoje_obserwowane_ogloszenia = driver.find_element(By.XPATH, "//h3[contains(text(),'Twoje obserwowane "
                                                                     "ogłoszenia')]")
        assert twoje_obserwowane_ogloszenia.text == "Twoje obserwowane ogłoszenia"
        driver.close()
