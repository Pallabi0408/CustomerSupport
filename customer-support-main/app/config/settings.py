import os

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
MODEL_DIR = os.path.join(BASE_DIR, 'model')
DATASET_DIR = os.path.join(BASE_DIR, 'dataset')
LOGS_DIR = os.path.join(BASE_DIR, 'logs')

CLASSIFIER_PATH = os.path.join(MODEL_DIR, 'classifier.pkl')
LABEL_ENCODER_PATH = os.path.join(MODEL_DIR, 'label_encoder.pkl')
SENTIMENT_MODEL_PATH = os.path.join(MODEL_DIR, 'sentiment_model.pkl')
SENTENCE_TRANSFORMER_MODEL_NAME = "all-MiniLM-L6-v2"
