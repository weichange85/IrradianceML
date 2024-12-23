from IrRegressionPrediction import logger
from IrRegressionPrediction.utils.common import read_yaml_file, create_directories
from IrRegressionPrediction.entity import PrepareBaseModelConfig
from pathlib import Path
import pandas as pd


class PrepBaseModel:
    def __init__(self, config: PrepareBaseModelConfig):
        self.config = config

    def get_base_model(self):
        pass




