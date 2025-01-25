from IrRegressionPrediction.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from IrRegressionPrediction.utils.common import read_yaml_file, create_directories
from IrRegressionPrediction.entity import DataIngestionConfig, PrepareBaseModelConfig, TrainingConfig
import os
from pathlib import Path

class ConfigurationManager:
    def __init__(
            self,
            config_filepath = CONFIG_FILE_PATH,
            param_filepath = PARAMS_FILE_PATH
    ):
        self.config = read_yaml_file(config_filepath)
        self.param = read_yaml_file(param_filepath)

        create_directories([self.config.artifacts_root])

    def getDataIngestionConfig(self) -> DataIngestionConfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        dataingestionconfig = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return dataingestionconfig
    
    def getPrepBaseModelConfig(self) -> PrepareBaseModelConfig:
        config = self.config.prep_base_model
        params = self.param
        create_directories([config.root_dir])

        prepbasemodelconfig = PrepareBaseModelConfig(
            root_dir=config.root_dir,
            base_model_path=config.base_model_path,
            n_estimators=params.N_ESTIMATORS,
            max_depth=params.MAX_DEPTH,
            learning_rate=params.LEARNING_RATE
        )

        return prepbasemodelconfig

    def getTrainingConfig(self) -> TrainingConfig:
        config = self.config.training
        base_model_config = self.config.prep_base_model
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "tableConvert.com_h52393.csv")
        params = self.param
        create_directories([Path(config.root_dir)])

        trainingConfig = TrainingConfig(
            root_dir=config.root_dir,
            trained_model_filepath=config.trained_model_filepath,
            base_model_path=base_model_config.base_model_path,
            training_data=Path(training_data),
            params_estimator=params #TODO: try to figure how to load in the estimator param
        )

        return trainingConfig