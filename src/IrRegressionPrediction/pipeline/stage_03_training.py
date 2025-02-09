from IrRegressionPrediction.config.configuration import ConfigurationManager
from IrRegressionPrediction.components.training import Training
from IrRegressionPrediction import logger

STAGE_NAME = "Training Stage"

class TrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        configManager = ConfigurationManager()
        trainingConfig = configManager.getTrainingConfig()
        training = Training(trainingConfig)
        training.training()


if __name__=="__main__":
    trainingPipeline = TrainingPipeline()
    trainingPipeline.main()
    #TODO: fix error, get rid of last row