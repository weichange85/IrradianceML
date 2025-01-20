from IrRegressionPrediction import logger
from IrRegressionPrediction.utils.common import read_yaml_file, create_directories
from IrRegressionPrediction.entity import PrepareBaseModelConfig
from pathlib import Path
import pandas as pd
from xgboost import XGBClassifier
import joblib
import sklearn



class PrepBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        self.model = XGBClassifier(
            n_estimators = self.config.n_estimators,
            max_depth = self.config.max_depth,
            learning_rate = self.config.learning_rate
        )

        # Save the base model without training it
        self.save_model(
            path = self.config.base_model_path,
            model = self.model
        )
    
    def save_mode(path, model):
         # Save the model instance (untrained) to a file using joblib
        joblib.dump(model, path)
