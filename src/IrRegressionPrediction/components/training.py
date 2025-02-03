from IrRegressionPrediction import logger
from IrRegressionPrediction.utils.common import read_yaml_file, create_directories
from IrRegressionPrediction.entity import TrainingConfig
from pathlib import Path
import pandas as pd
from xgboost import XGBClassifier
from sklearn.model_selection import GridSearchCV, train_test_split
import joblib

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self):

        """get base model from prep_base_model.py"""
        
        self.model = joblib.load(
            self.config.base_model_path
        )

    def load_data(self) -> pd.DataFrame:
        """
        Load in data from artifacts/data_ingestion/data
        """
        input_data = pd.read_csv(
            self.config.training_data,
            header=1
        )
        return input_data
    
    def data_prep(self):
        """
        Clean and prepare the data for training, return X and Y varaibles.
        """
        raw_data = self.load_data()
        raw_data = raw_data.dropna().reset_index(drop=True).drop(columns=["|"], errors="ignore")
        X = raw_data.drop(columns=["DATE (MM/DD/YYYY)", "TOT Global Horiz [kW-hr/m^2]"])
        Y = raw_data["TOT Global Horiz [kW-hr/m^2]"]
        return X, Y

    def define_grid_search(self):
        """
        Define and return the grid_search
        """
        param_grid = self.config.params_grid
        grid_search = GridSearchCV(
            estimator=self.model,
            param_grid=param_grid,
            scoring=self.config.params_scoring,
            cv=self.config.params_cv,
            verbose=self.config.params_verbose,
            n_jobs=self.config.params_n_jobs
        )

        return grid_search
    
    def perform_grid_search(self, grid_search, X, Y):
        """
        Fits GridSearchCV on the training data.
        """
        grid_search.fit(X,Y)
        return grid_search.best_estimator_
    
    def save_trained_model(self, model):
        """
        Save the best trained model to artifacts folder.
        """
        joblib.dump(model, self.config.trained_model_filepath)

    def training(self):
        """
        Main method to execute the training process.
        """
        self.get_base_model()
        X,Y = self.data_prep()

        grid_search = self.define_grid_search()
        best_model = self.perform_grid_search(grid_search, X, Y)

        self.save_trained_model(best_model)
        logger.info(f"Best Model Saved at {self.config.trained_model_filepath}")

