import logging
import os
import sys
import pandas as pd

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
from Scripts.processdata_browser import save_to_sqlite
from Scripts.process_items import process_items

def main():
    """
    Función principal que inicia el script de automatización.
    """
    try:
        logger.info("Starting the automation script")
        
        login_url = "https://acme-test.uipath.com/login"
        work_items_url = "https://acme-test.uipath.com/work-items"
        process_base_url = "https://acme-test.uipath.com/work-items/update"
        browser_name = "chrome"
        
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

        # Guardar los datos en la base de datos SQLite
        db_file = "Data/PythonAutomation.db"  # Especifica la ruta al archivo de la base de datos
        table_name = "ACME_Systems"  # Nombre de la tabla
        save_to_sqlite(df, db_file, table_name)
        
        # Procesar cada elemento de trabajo
        work_items = df.to_dict(orient="records")
        process_items(driver, process_base_url, work_items)

        # Cerrar el navegador
        close_browser(driver)

        logger.info("Automation script completed successfully")
    except Exception as e:
        logger.error("An error occurred in the main script", exc_info=True)

if __name__ == "__main__":
    main()
