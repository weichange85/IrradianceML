import numpy as np
import pandas as pd
import joblib
import os

class PredictionPipeline:
    def __init__(self, input_features: dict):
        self.input_features = input_features

    def load_model(self):
        """Load the trained regression model."""
        model_path = os.path.join("artifacts", "training", "model.xgb")
        model = joblib.load(model_path)
        return model

    def preprocess_input(self):
        """Convert input dictionary to a DataFrame suitable for prediction."""
        expected_features = [
            'MAX Global Horiz (W/m^2)', 'TOT Direct Normal (kW-hr/m^2)',
            'MAX Direct Normal (W/m^2)', 'TOT Diffuse Horiz (calc) (kW-hr/m^2)',
            'MAX Diffuse Horiz (calc) (W/m^2)', 'AVG Dry Bulb Temp (deg C)',
            'MAX Dry Bulb Temp (deg C)', 'MIN Dry Bulb Temp (deg C)',
            'AVG Rel Humidity (%)', 'MAX Rel Humidity (%)', 'MIN Rel Humidity (%)',
            'AVG Avg Wind Speed @ 10ft (m/s)', 'MAX Avg Wind Speed @ 10ft (m/s)',
            'MIN Avg Wind Speed @ 10ft (m/s)', 'AVG Precipitation (mm)',
            'MAX Precipitation (mm)', 'MIN Precipitation (mm)',
            'AVG Zenith Angle (degrees)', 'MAX Zenith Angle (degrees)',
            'MIN Zenith Angle (degrees)', 'AVG Azimuth Angle (degrees)',
            'MAX Azimuth Angle (degrees)', 'MIN Azimuth Angle (degrees)'
        ]

        # Ensure the input is in the correct order
        data = {feature: self.input_features.get(feature, 0) for feature in expected_features}
        return pd.DataFrame([data])

    def predict(self):
        """Generate prediction."""
        model = self.load_model()
        processed_input = self.preprocess_input()
        prediction = model.predict(processed_input)
        return prediction[0]

if __name__ == "__main__":
    # Example input
    input_features = {
        'MAX Global Horiz (W/m^2)': 800,
        'TOT Direct Normal (kW-hr/m^2)': 4.5,
        'MAX Direct Normal (W/m^2)': 950,
        'TOT Diffuse Horiz (calc) (kW-hr/m^2)': 2.3,
        'MAX Diffuse Horiz (calc) (W/m^2)': 300,
        'AVG Dry Bulb Temp (deg C)': 25,
        'MAX Dry Bulb Temp (deg C)': 30,
        'MIN Dry Bulb Temp (deg C)': 20,
        'AVG Rel Humidity (%)': 50,
        'MAX Rel Humidity (%)': 70,
        'MIN Rel Humidity (%)': 30,
        'AVG Avg Wind Speed @ 10ft (m/s)': 3,
        'MAX Avg Wind Speed @ 10ft (m/s)': 5,
        'MIN Avg Wind Speed @ 10ft (m/s)': 1,
        'AVG Precipitation (mm)': 0,
        'MAX Precipitation (mm)': 0,
        'MIN Precipitation (mm)': 0,
        'AVG Zenith Angle (degrees)': 45,
        'MAX Zenith Angle (degrees)': 60,
        'MIN Zenith Angle (degrees)': 30,
        'AVG Azimuth Angle (degrees)': 180,
        'MAX Azimuth Angle (degrees)': 200,
        'MIN Azimuth Angle (degrees)': 160
    }

    predictor = PredictionPipeline(input_features)
    result = predictor.predict()
    print(f"Predicted TOT Global Horiz [kW-hr/m^2]: {result}")