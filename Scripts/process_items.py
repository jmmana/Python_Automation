from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import logging

logger = logging.getLogger(__name__)

def process_items(driver, base_url, work_items):
    """
    Procesa cada elemento de trabajo abriendo una nueva pestaña y navegando a la URL específica del elemento.

    Args:
        driver (WebDriver): El controlador del navegador.
        base_url (str): La URL base para procesar los elementos de trabajo.
        work_items (list): Una lista de diccionarios con los datos de los elementos de trabajo.
    """
    try:
        logger.info("Starting to process work items")

        for item in work_items:
            wiid = item["WIID"]
            item_url = f"{base_url}/{wiid}"
            logger.info(f"Processing work item: {wiid}")

            # Abrir una nueva pestaña
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[-1])

            # Navegar a la URL del elemento de trabajo
            driver.get(item_url)

            # Aquí puedes agregar el código para procesar el elemento de trabajo
            # Por ejemplo, interactuar con los elementos de la página, extraer datos, etc.

            # Cerrar la pestaña
            driver.close()
            driver.switch_to.window(driver.window_handles[0])

        logger.info("Processing of work items completed successfully")
    except Exception as e:
        logger.error("Failed to process work items", exc_info=True)

if __name__ == "__main__":
    import sys
    from selenium import webdriver
    import pandas as pd

    if len(sys.argv) != 3:
        logger.error("Usage: python process_items.py <base_url> <input_file>")
        sys.exit(1)

    base_url = sys.argv[1]
    input_file = sys.argv[2]

    df = pd.read_csv(input_file)
    work_items = df.to_dict(orient="records")

    driver = webdriver.Chrome()
    driver.maximize_window()

    process_items(driver, base_url, work_items)

    driver.quit()
