from flask import Flask, request, jsonify
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Load and prepare the data
df = pd.read_csv("BostonHousing.csv")
x = df.drop("medv", axis=1)
y = df["medv"]
x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=42
)

# Train models
linear_model = LinearRegression().fit(x_train, y_train)
forest_model = RandomForestRegressor(random_state=42).fit(x_train, y_train)

app = Flask(__name__)


@app.route("/")
def home():
    return "Boston Housing Model API is running!"


@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    features = pd.DataFrame([data])

    linear_pred = linear_model.predict(features)[0]
    forest_pred = forest_model.predict(features)[0]

    return jsonify(
        {"Linear Prediction": linear_pred, "Random Forest Prediction": forest_pred}
    )


if __name__ == "__main__":
    app.run(debug=True)
