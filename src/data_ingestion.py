import pandas as pd
from sklearn.model_selection import train_test_split
import os
import logging
import yaml

dir = 'log'
os.makedirs(dir,exist_ok=True)

logger = logging.getLogger('data_ingestion')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

log_file_path = os.path.join(dir,'data_ingestion.log')
file_handler = logging.FileHandler(log_file_path)
file_handler.setLevel('DEBUG')

formater = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger.addHandler(console_handler)
logger.addHandler(file_handler)

def load_params(params_path:str) -> dict:
    try:
        with open(params_path, 'r') as file:
            params = yaml.safe_load(file)
        logger.debug('Parametes are retreived from %s', params_path)
        return params
    except FileNotFoundError as e:
        logger.error('File not found at %s', params_path)
        raise
    except yaml.YAMLError as e:
        logger.error('YAML error: %s', e)
        raise
    except Exception as e:
        logger.error('Unexpected error %s', e)
        raise