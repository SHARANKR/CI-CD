import pandas as pd
import os
import logging
import yaml


dir = 'log'
os.makedirs(dir, exist_ok=True)

logger = logging.getLogger('preprocessing')
logger.setLevel('DEBUG')

console_handler = logging.StreamHandler()
console_handler.setLevel('DEBUG')

data_path = os.path.join(dir, 'Preprocessing.log')
file_handler = logging.FileHandler(data_path)
file_handler.setLevel('DEBUG')

logger.addHandler(console_handler)
logger.addHandler(file_handler)

