import logging
import os
import sys
from Scripts.open_browser import open_browser

# Configure logging
log_dir = os.path.join(os.path.dirname(__file__), 'logs')
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

def main():
    try:
        logger.info("Starting the automation script")
        
        # URL to open
        url = "https://www.example.com"
        
        # Call the open_browser function
        open_browser(url)
        
        logger.info("Automation script completed successfully")
    except Exception as e:
        logger.error("An error occurred in the main script", exc_info=True)

if __name__ == "__main__":
    main()
