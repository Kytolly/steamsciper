import requests

from src.utils.logger import getMyLogger
logger = getMyLogger()

def get_response(url):
    headers = {
            "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/85.0.4183.102 Safari/537.36', 'Accept-Language': 'zh-CN '
    }
    
    try:
        response = requests.get(url, headers=headers)
        logger.info("src/scraper/parser.py: Getting text from url: %s", url)
        return response
    
    except requests.RequestException as e:
        logger.error("src/scraper/parser.py: Failed to get text from url: %s", url)
        logger.error(e)
        return None
    