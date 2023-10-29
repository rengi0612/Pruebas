from lib.driver import Browser
from selenium.webdriver.common.by import By
from collections import namedtuple
from time import sleep

Locator = namedtuple('Locator', ['by', 'value'])

class BasePage(object):

    url = "https://sitmar.dimar.mil.co/test/"

    def __init__(self, driver):
        self.driver = driver
        self.Browser = Browser

    @property
    def inspecciones(self):
        return self.Browser(self.driver, Locator(By.XPATH, value='//span[contains(text(),"Inspecciones")]'))

    @property
    def empServicios(self):
        return self.Browser(self.driver, Locator(By.XPATH, value='//a[@title="Empresas de Servicios"]'))

    @property
    def log_in_button(self):
        return self.Browser(self.driver, Locator(By.XPATH, value='//button[@class="btn btn-block btn-success"]'))

    @property
    def input_user(self):
        return self.Browser(self.driver, Locator(By.XPATH, value='//input[@name="username"]'))
    
    @property
    def input_password(self):
        return self.Browser(self.driver, Locator(By.XPATH, value='//input[@name="password"]'))
    
    def log_in(self):
        try:
            self.driver.get(self.url)
            sleep(2)
            self.log_in_button.click()
            sleep(1)
            self.input_user.set_text("1111222333-01")
            sleep(1)
            self.input_password.set_text("Dimar2023*")
            sleep(10)
        except Exception as e:
            print("Error while log in: {}".format(e))

    def go_to(self):
        try:
            self.inspecciones.click()
            sleep(10)
            self.empServicios.click()
        except Exception as e:
            print("Error navigating to Empresas de Servicios: {}".format(e))
