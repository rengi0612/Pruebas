import os
import json
import platform
import time
from pathlib import Path
from time import sleep
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.webdriver.common import keys as K
from typing import Any

class Browser(object):

    def __init__(self, driver, locator):
        self.driver = driver
        self.locator = locator

    @classmethod
    def setup(self) -> Any:
        path = str(Path(os.getcwd()).parent.parent) + "/Pruebas/chromedriver"
        chrome_options = ChromeOptions()
        global driver
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_prefs = {}
        chrome_options.experimental_options["prefs"] = chrome_prefs
        chrome_prefs["profile.default_content_settings"] = {"images": 2}
        chrome_desired_caps = DesiredCapabilities.CHROME
        chrome_desired_caps['goog:loggingPrefs'] = { 'browser':'ALL' }
        driver = webdriver.Chrome(executable_path=path, chrome_options=chrome_options, desired_capabilities=chrome_desired_caps)
        driver.maximize_window()
        driver.set_window_position(0, 0)
        driver.set_window_size(1280, 720)
        return driver

    @classmethod
    def driver_tear_down(cls, driver: webdriver):
        cls.browser_logs(driver)
        try:
            driver.quit()
        except Exception as e:
            print("Error trying quit browser: {}".format(e))

    def get_current_url(self) -> str:
        return self.driver.current_url

    def browser_refresh(self) -> None:
        self.driver.refresh()

    def wait_to_be_clickable(self, wait_time: int = 10):
        try:
            web_element = WebDriverWait(self.driver, wait_time).until(
                    EC.element_to_be_clickable(self.locator)
                )
            return web_element
        except Exception as e:
            print("Error locating element: {}".format(e))

    def find_by_visibility(self, wait_time: int = 10):
        try:
            web_element = WebDriverWait(self.driver, wait_time).until(
                    EC.visibility_of_element_located(self.locator)
                )
            return web_element
        except Exception as e:
            print("Error locating element: {}".format(e))

    def exists_by_presence(self,wait_time: int = 10) -> bool:
        try:
                WebDriverWait(self.driver, wait_time).until(
                    EC.presence_of_all_elements_located(locator=self.locator)
                )
                return True
        except TimeoutException:
            return False
    
    def find_by_visibility_list(self,wait_time: int = 10):
        try:
            web_element = WebDriverWait(self.driver, wait_time).until(
                    EC.visibility_of_all_elements_located(self.locator)
                )
            return web_element
        except Exception as e:
            print("Error locating element: {}".format(e))
    
    def click(self) -> None:
        try:
            web_element = self.wait_to_be_clickable()
            web_element.click()
            return None
        except Exception as e:
            print("Error trying to perform a click: {}".format(e))

    def set_text(self,txt) -> None:
        try:
            web_element = self.find_by_visibility()
            web_element.send_keys(txt)
            return None
        except Exception as e:
            print("Error setting text: {}".format(e))

    def get_attribute(self, attr:str) -> Any:
        try:
            web_element = self.find_by_visibility()
            attribute = web_element.get_attribute(attr)
            return attribute
        except Exception as e:
            print("Error getting attribute: {}".format(e))