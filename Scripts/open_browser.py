import webbrowser
import logging

logger = logging.getLogger(__name__)

def open_browser(url):
    try:
        logger.info(f"Attempting to open URL: {url}")
        webbrowser.open(url)
        logger.info(f"Successfully opened URL: {url}")
    except Exception as e:
        logger.error(f"Failed to open URL: {url}", exc_info=True)

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        logger.error("Usage: python open_browser.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    open_browser(url)
