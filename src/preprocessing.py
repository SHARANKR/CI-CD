import pandas as pd
import os
import logging
import yaml
from sklearn.preprocessing import LabelEncoder
import nltk
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import string

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

def transform_text(text):

    ps = PorterStemmer()
    text = text.lower()
    text = nltk.word_tokenize(text)
    text = [word for word in text if word.isalnum()]
    text = [word for word in text if word not in stopwords.word('English') and word not in string.punctuation]
    text = [ps.stem(word) for word in text ]
    return " ".join(text)

def preprocess(df, text_column='text', target_column='target'):
    try:
        logger.debug('Preprocessing of the dataset started')
        encoder = LabelEncoder()
        df[target_column] = encoder.fit_transform(df[target_column])
        logger.debug('Target_column is encoded')
        
        df = df.drop_duplicates(keep = 'first')
        logger.debug('Duplicates removed')
        
        df.loc[:, text_column] = df[text_column].apply(transform_text)
        logger.debug('Text_column is transformed')
        return df
    except KeyError as e:
        logger.error('Column not found %s', e)
        raise
    except Exception as e:
        logger.error('Error during text normalization: %s', e)
        raise
    
        