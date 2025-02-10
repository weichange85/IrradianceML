from IrRegressionPrediction import logger
from IrRegressionPrediction.utils.common import read_yaml_file, create_directories
from IrRegressionPrediction.entity import ModelEvaluationConfig

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config