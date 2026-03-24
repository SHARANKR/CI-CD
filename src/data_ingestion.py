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
    
def load_data(load_path:str) -> pd.DataFrame:
    try:
        df = pd.read_csv(load_path)
        logger.debug('Data has been loaded %s', load_path)
        return df
    except pd.errors.ParserError as e:
        logger.error('Failed to parse the csv file %s', e)
        raise
    except Exception as e:
        logger.error('Unexpected error raised while loadind data %s', e)
        raise
    
def preprocess(df:pd.DataFrame) -> pd.DataFrame:
    try:
        df.drop(columns = ['Unnamed2','Unnamed3','Unnamed4'],inplace=True)
        df.rename(columns = {'v1':'target','v2':'text'},inplace=True)
        logger.debug('Data preprocessing completed')
        return df
    except KeyError as e:
        logger.error('Missing column in the dataframe %s', e)
        raise
    except Exception as e:
        logger.error("Unexpected error raised during data preprocessing %s", e)
        raise