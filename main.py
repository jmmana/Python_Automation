import logging
import os
import sys

# Agregar el directorio del proyecto al sys.path
# Esto permite que Python encuentre los módulos en el directorio del proyecto.
sys.path.append(os.path.dirname(__file__))

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
    format='%(asctime)s - %(name)-30s - %(levelname)-8s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

# Crear un logger con el nombre del módulo actual.
logger = logging.getLogger(__name__)

# Importar la función open_browser desde el módulo scripts.open_browser.
from scripts.open_browser import open_browser

def main():
    try:
        # Registrar un mensaje de información indicando el inicio del script.
        logger.info("Starting the automation script")
        
        # URL a abrir
        url = "https://www.example.com"
        
        # Llamar a la función open_browser con la URL proporcionada.
        open_browser(url)
        
        # Registrar un mensaje de información indicando que el script se completó con éxito.
        logger.info("Automation script completed successfully")
    except Exception as e:
        # Registrar un mensaje de error si ocurre una excepción.
        # exc_info=True incluye la traza del error en el log.
        logger.error("An error occurred in the main script", exc_info=True)

# Si el script se ejecuta directamente (no importado como módulo), llamar a la función main.
if __name__ == "__main__":
    main()
