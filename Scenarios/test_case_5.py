import sys
sys.path.append("/Users/juan.rengifo/Desktop/Personal/U/Pruebas/automata/Pruebas")
from Pages.base import BasePage
from Pages.servicio import ServicioPage
from lib.driver import Browser
from time import sleep


def main():
    try:
        driver = Browser.setup()

        base = BasePage(driver)
        servicio = ServicioPage(driver)
        base.log_in()
        sleep(10)
        base.go_to()
        sleep(5)

        if servicio.validate_empresa(empresa='AUSTRALIAN SHIP LOGISTICS O.P. S.A.S.'):
            print("Registros de empresa encontrados")
        else:
            print("No se encontraron registros")
    except Exception as e:
        print("Error en el test case 5: {}".format(e))

if __name__ == "__main__":
    main()