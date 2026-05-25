import joblib
import numpy as np

model = joblib.load("model/model.pkl")

def predict_fault(data):
    features = np.array([
        data["Va"], data["Vb"], data["Ia"], data["Ib"]
    ]).reshape(1, -1)

    return int(model.predict(features)[0])
