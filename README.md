# Pruebas
Este proyecto está diseñado para automatizar las pruebas funcionales del producto SIMART, en su ambiente de pruebas.

## Cómo ejecutar?

- Clonar el repo en local
- Descargar la versión de Chromedriver que se ajuste a su versión de chrome
- Colocar el chromdriver en la raíz del proyecto
- Actualizar la línea 2 de cada scenario con el path que lo lleve a la ubicación donde tenga el repo en local
- Correr el scenario: python3 test_case_1.py
- Durante la ejecución deberá ingresar el captcha cuando esté en el inicio de sesión y dar click en ingresar, el scenario se encargará del resto

## Casos

- Los casos automatizados que se encuentran son el 1,2 y 5.

1. Se llena los campos de Nit y Nombre de empresa, luego se da click en limpiar y se valida que los campos vuelvan a estar vacios
2. Se valida la presencia de registros por defecto al cargar la página
5. Se prueba la búsqueda de registro por empresa.

