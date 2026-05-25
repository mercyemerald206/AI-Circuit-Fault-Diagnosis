from fastapi import FastAPI
from inference import predict_fault

app = FastAPI()

@app.post("/predict")
def predict(data: dict):
    result = predict_fault(data)
    return {"fault_prediction": result}
