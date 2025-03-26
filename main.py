import logging
import os
import sys
from datetime import datetime

# Configuración del logging
log_dir = os.path.join(os.path.dirname(__file__), 'logs')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'automation.log')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)-45s - %(levelname)-8s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

from Scripts.open_browser import open_browser
from Scripts.close_browser import close_browser
from Scripts.login_browser import login
from Scripts.datascraping_browser import scrape_work_items
from Scripts.processdata_browser import save_to_csv

def main():
    """
    Función principal que inicia el script de automatización.
    """
    try:
        logger.info("Starting the automation script")
        
        # URL de login y de trabajo
        login_url = "https://acme-test.uipath.com/login"
        work_items_url = "https://acme-test.uipath.com/work-items"
        
        # Nombre del navegador a usar
        browser_name = "chrome"
        
        # Llamar a la función open_browser con la URL de login y el nombre del navegador
        driver = open_browser(login_url, browser_name)

        # Credenciales de login
        username = "jmmana@gmail.com"
        password = "P@ssWoor!d"

        # Llamar a la función de login
        login(driver, username, password)

        # Llamar a la función de scraping
        df = scrape_work_items(driver, work_items_url)

        # Guardar los datos en un archivo CSV en el directorio Data
        output_directory = "Data"
        save_to_csv(df, output_directory)

        # Cerrar el navegador
        close_browser(driver)

        logger.info("Automation script completed successfully")
    except Exception as e:
        logger.error("An error occurred in the main script", exc_info=True)

if __name__ == "__main__":
    main()
