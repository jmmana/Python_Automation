import webbrowser
import logging
import os
import sys

# Configure logging
log_dir = os.path.join(os.path.dirname(__file__), '..', 'logs')
os.makedirs(log_dir, exist_ok=True)
log_file = os.path.join(log_dir, 'automation.log')

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger(__name__)

def open_browser(url):
    try:
        logger.info(f"Attempting to open URL: {url}")
        webbrowser.open(url)
        logger.info(f"Successfully opened URL: {url}")
    except Exception as e:
        logger.error(f"Failed to open URL: {url}", exc_info=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        logger.error("Usage: python open_browser.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    open_browser(url)
