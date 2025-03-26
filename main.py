import logging
import os
import sys

# Configuración del logging
# Definir el directorio donde se guardarán los archivos de log.
log_dir = os.path.join(os.path.dirname(__file__), 'logs')
# Crear el directorio de logs si no existe.
os.makedirs(log_dir, exist_ok=True)
# Definir el archivo de log.
log_file = os.path.join(log_dir, 'automation.log')

# Configurar el logging básico.
# - level: Nivel de logging (DEBUG, INFO, WARNING, ERROR, CRITICAL).
# - format: Formato de los mensajes de log.
#   - %(asctime)s: Fecha y hora del log.
#   - %(name)-30s: Nombre del logger, ajustado a 30 caracteres.
#   - %(levelname)-8s: Nivel del log, ajustado a 8 caracteres.
#   - %(message)s: Mensaje del log.
# - handlers: Destinos de los mensajes de log.
#   - FileHandler: Guarda los logs en un archivo.
#   - StreamHandler: Muestra los logs en la consola.
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)-45s - %(levelname)-8s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

# Crear un logger con el nombre del módulo actual.
logger = logging.getLogger(__name__)

# Importar la función open_browser desde el módulo scripts.open_browser.
from Scripts.open_browser import open_browser
from Scripts.close_browser import close_browser
from Scripts.login_browser import login


def main():
    """
    Función principal que inicia el script de automatización.
    """
    try:
        logger.info("Starting the automation script")
        
        # URL a abrir
        url = "https://acme-test.uipath.com/login"
        
        # Nombre del navegador a usar (por ejemplo, 'chrome' o 'firefox').
        browser_name = "chrome"
        
        # Llamar a la función open_browser con la URL y el nombre del navegador.  
        driver = open_browser(url, browser_name)

        # Credenciales de login
        username = "jmmana@gmail.com"
        password = "P@ssWoor!d"

        # Llamar a la función de login
        login(driver, username, password)

        # Cerrar el navegador
        close_browser(driver)


        logger.info("Automation script completed successfully")
    except Exception as e:
        logger.error("An error occurred in the main script", exc_info=True)

# Si el script se ejecuta directamente (no importado como módulo), llamar a la función main.
if __name__ == "__main__":
    main()
