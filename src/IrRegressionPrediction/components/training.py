from IrRegressionPrediction import logger
from IrRegressionPrediction.utils.common import read_yaml_file, create_directories
from IrRegressionPrediction.entity import PrepareBaseModelConfig
from pathlib import Path
import pandas as pd
from xgboost import XGBClassifier
import joblib

class Training:
    def __init__(self):
        config = 