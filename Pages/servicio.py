from operator import and_
from lib.driver import Browser
from selenium.webdriver.common.by import By
from collections import namedtuple
from time import sleep

Locator = namedtuple('Locator', ['by', 'value'])

class ServicioPage(object):

    def __init__(self, driver):
        self.driver = driver
        self.Browser = Browser

    @property
    def nit_input(self):
        return self.Browser(self.driver, Locator(By.XPATH, value='//input[@formControlname="nitFiltro"]'))

    @property
    def empresa_input(self):
        return self.Browser(self.driver, Locator(By.XPATH, value='//input[@formControlname="nombreEmpresaFiltro"]'))

    @property
    def registros(self):
        return self.Browser(self.driver, Locator(By.XPATH, value='//table[@id="tbSolicitud"]/tbody/tr'))

    @property
    def fecha_inicio_input(self):
        return self.Browser(self.driver, Locator(By.XPATH, value='//input[@id="fechaInicioFiltro"]'))
    
    @property
    def fecha_fin_input(self):
        return self.Browser(self.driver, Locator(By.XPATH, value='//input[@id="fechaFinFiltro"]'))

    @property
    def limpiar_button(self):
        return self.Browser(self.driver, Locator(By.XPATH, value='//button[@class="btn btn-labeled btn-warning btn-sm"]'))

    @property
    def consultar_button(self):
        return self.Browser(self.driver, Locator(By.XPATH, value='//button[@class="btn btn-labeled btn-success btn-sm"]'))

    @property
    def empresa_title_registros(self):
        return self.Browser(self.driver, Locator(By.XPATH, value='//table[@id="tbSolicitud"]/tbody/tr/td[@class=" dt-head-center"]'))
    
    def find_registros(self) -> bool:
        return self.registros.exists_by_presence()

    def input_all_fields(self):
        try:
            sleep(2)
            #self.fecha_inicio_input.set_text('28/08/2023')
            #self.fecha_fin_input.set_text('29/08/2023')
            self.nit_input.set_text('123456789')
            self.empresa_input.set_text('Empresa')
        except Exception as e:
            print("Error setting fields: {}".format(e))

    def clean_validate(self) -> bool:
        try:
            sleep(1)
            self.limpiar_button.click()
            sleep(5)
            print(self.nit_input.get_attribute("innerText"))
            print(self.empresa_input.get_attribute("innerText"))
            if (self.nit_input.get_attribute("innerText") == ''):
                if(self.empresa_input.get_attribute("innerText") == ''):
                    return True
            return False
        except Exception as e:
            print("Error validating and cleaning: {}".format(e))

    def validate_empresa(self, empresa) -> bool:
        try:
            sleep(1)
            self.empresa_input.set_text(empresa)
            sleep(1)
            self.consultar_button.click()
            sleep(5)
            registros = self.empresa_title_registros.find_by_visibility_list()
            for reg in registros:
                if(reg.get_attribute("innerText") == empresa):
                    return True
            return False
        except Exception as e:
            print("Error validating empresa: {}".format(e))


