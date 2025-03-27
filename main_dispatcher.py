import logging
import os
import sys
import pandas as pd
from dotenv import load_dotenv

# Cargar las variables de entorno desde el archivo .env
load_dotenv()

# Acceder a las variables de entorno
login_url = os.getenv('LOGIN_URL')
work_items_url = os.getenv('WORK_ITEMS_URL')
browser_name = os.getenv('BROWSER_NAME')
username = os.getenv('USERNAME')
password = os.getenv('PASSWORD')

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

def main():
    """
    Función principal que inicia el script de automatización.
    """
    try:
        logger.info("Starting the automation script")
        
        driver = open_browser(login_url, browser_name)

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
        
        # Cerrar el navegador
        close_browser(driver)

        logger.info("Automation script completed successfully")
    except Exception as e:
        logger.error("An error occurred in the main script", exc_info=True)

if __name__ == "__main__":
    main()
