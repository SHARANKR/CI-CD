import pandas as pd
from sklearn.model_selection import train_test_split
import os
import logging

dir = 'log'
os.makedirs(dir,exist_ok=True)

logger = logging.getLogger('data_ingestion')
logger.setLevel('DEBUG')