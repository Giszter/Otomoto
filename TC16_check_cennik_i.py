import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

service = Service("C:\\Users\\Hubert\\Downloads\\chromedriver.exe")
driver = webdriver.Chrome(service=service)


class cennik_i(unittest.TestCase):
    def test_cennik_i(self):
        driver.get("https://www.otomoto.pl/")
        driver.implicitly_wait(10)
        driver.maximize_window()
        driver.find_element(By.XPATH, "//button[@id='onetrust-accept-btn-handler']").click()
        main_page = driver.current_window_handle
        driver.find_element(By.XPATH, "//a[normalize-space()='Cennik dla Klientów Indywidualnych']").click()
        for window_handle in driver.window_handles:
            if window_handle != main_page:
                driver.switch_to.window(window_handle)
        print(driver.current_url)
        assert driver.current_url == "https://pomoc.otomoto.pl/hc/pl/articles/216416787-Cennik-dla-Klient%C3%B3w" \
                                     "-Indywidualnych"
        driver.quit()
