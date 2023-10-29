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
        servicio.input_all_fields()
        sleep(5)
        servicio.limpiar_button.click()
        sleep(5)
        if servicio.clean_validate():
            print("Limpio")
        else:
            print("No vacio")
    except Exception as e:
        print("Error en el test case 1: {}".format(e))

if __name__ == "__main__":
    main()