from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path

@dataclass(frozen=True)
class PrepareBaseModelConfig:
    root_dir: Path
    base_model_path: Path
    n_estimators: int
    max_depth:int
    learning_rate:int 

@dataclass(frozen=True)
class TrainingConfig:
    root_dir: Path
    trained_model_filepath: Path
    base_model_path: Path
    training_data: Path
    params_grid: dict
    params_scoring: str
    params_cv: int
    params_verbose: int
    params_n_jobs: int

@dataclass(frozen=True)
class ModelEvaluationConfig:
    model_path: Path
    pass ##TODO##