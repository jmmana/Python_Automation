import pandas as pd
import logging
import os
from datetime import datetime

logger = logging.getLogger(__name__)

def save_to_csv(df, directory):
    """
    Guarda un DataFrame en un archivo CSV en el directorio especificado.

    Args:
        df (DataFrame): El DataFrame a guardar.
        directory (str): El directorio donde se guardará el archivo CSV.
    """
    try:
        # Crear el directorio si no existe
        os.makedirs(directory, exist_ok=True)

        # Generar el nombre del archivo con la fecha y hora actuales
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"Example_{timestamp}.csv"
        filepath = os.path.join(directory, filename)

        # Guardar el DataFrame en un archivo CSV
        df.to_csv(filepath, index=False)
        logger.info(f"Data saved to {filepath} successfully")
    except Exception as e:
        logger.error(f"Failed to save data to {filepath}", exc_info=True)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        logger.error("Usage: python processdata_browser.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_directory = "Data"

    df = pd.read_csv(input_file)
    save_to_csv(df, output_directory)
