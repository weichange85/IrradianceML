from IrRegressionPrediction.config.configuration import ConfigurationManager
from IrRegressionPrediction.components.prep_base_model import PrepBaseModel
from IrRegressionPrediction import logger

STAGE_NAME = "Prep Base Model Stage"

class PrepBaseModelPipeline:
    def __init__(self):
        pass

    def main(self):
        configManager = ConfigurationManager()
        prepBaseModelConfig = configManager.getPrepBaseModelConfig()
        prepBaseModel = PrepBaseModel(prepBaseModelConfig)
        prepBaseModel.get_base_model()


if __name__ == "__main__":
    prepBaseModelPipeline = PrepBaseModelPipeline()
    prepBaseModelPipeline.main()