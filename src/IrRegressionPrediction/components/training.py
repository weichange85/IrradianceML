from IrRegressionPrediction import logger
from IrRegressionPrediction.utils.common import read_yaml_file, create_directories
from IrRegressionPrediction.entity import TrainingConfig
from pathlib import Path
import pandas as pd
from xgboost import XGBClassifier
import joblib

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self):
        pass 