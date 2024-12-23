from IrRegressionPrediction.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from IrRegressionPrediction.utils.common import read_yaml_file, create_directories
from IrRegressionPrediction.entity import DataIngestionConfig

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
            unzip_dir=config.unzip_dir,
        )

        return dataingestionconfig
