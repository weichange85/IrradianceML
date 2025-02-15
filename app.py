from flask import Flask, render_template, request
import joblib
import numpy as np
from IrRegressionPrediction.pipeline.prediction import PredictionPipeline

app = Flask(__name__)

# Define feature names (must match the expected input)
FEATURES = [
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

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None

    if request.method == "POST":
        try:
            # Convert input data from form to dictionary
            input_data = {feature: float(request.form.get(feature, 0)) for feature in FEATURES}

            # Use PredictionPipeline to generate prediction
            predictor = PredictionPipeline(input_features=input_data)
            prediction = predictor.predict()
        except Exception as e:
            prediction = f"Error: {str(e)}"

    return render_template("index.html", prediction=prediction, features=FEATURES)

if __name__ == "__main__":
    app.run(debug=True)

    ##TODO## Missing input turns into mean or dropped