import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\Hubert\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service=service)


class akademia(unittest.TestCase):
    def test_akademia(self):
        driver.get("https://www.otomoto.pl/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
        main_page = driver.current_window_handle
        driver.find_element(By.XPATH, "//a[normalize-space()='Akademia Rozwoju Dealera']").click()
        for window_handle in driver.window_handles:
            if window_handle != main_page:
                driver.switch_to.window(window_handle)

        assert driver.current_url == "https://akademia.otomoto.pl/"
        driver.quit()
