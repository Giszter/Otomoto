import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\Hubert\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service=service)


class regulamin_biznes(unittest.TestCase):
    def test_regulamin_biznes(self):
        driver.get("https://www.otomoto.pl/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
        driver.find_element(By.XPATH, "//a[normalize-space()='Regulamin dla Klientów Biznesowych']").click()

        assert driver.title == "Regulamin dla Klientów Biznesowych – Centrum Pomocy"
        driver.close()
