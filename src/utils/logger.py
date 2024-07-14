import logging
import logging.config
import json

def getMyLogger():
    config_path = 'config/logging_config.json'
    
    with open(config_path, 'r') as f:
        config = json.load(f)
        logging.config.dictConfig(config)
    
    return logging.getLogger('my_logger')