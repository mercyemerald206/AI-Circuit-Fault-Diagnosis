from fastapi import FastAPI
import numpy as np

app = FastAPI(title="Fault Diagnosis Service")

@app.post("/predict")
def predict(data: dict):
    v = data["voltage"]
    i = data["current"]

    # simple anomaly score (placeholder for ML model)
    score = abs(v - i) / (v + 1e-6)

    return {
        "fault_score": float(score),
        "status": "FAULT" if score > 0.6 else "NORMAL"
    }
