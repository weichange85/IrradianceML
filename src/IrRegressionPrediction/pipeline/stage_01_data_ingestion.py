from IrRegressionPrediction.config.configuration import ConfigurationManager
from IrRegressionPrediction.components.data_ingestion import DataIngestion
from IrRegressionPrediction import logger

STAGE_NAME = "Data Ingestion Stage"

class DataIngestionPipeline:
    def __init__(self):
        pass

    def main(self):
        configManager = ConfigurationManager()
        dataIngestionConfig = configManager.getDataIngestionConfig()
        dataIngestion = DataIngestion(dataIngestionConfig)
        dataIngestion.download_file()
        dataIngestion.extract_zip_file()


if __name__ == "__main__":
    dataIngestionPipeline = DataIngestionPipeline()
    dataIngestionPipeline.main()
