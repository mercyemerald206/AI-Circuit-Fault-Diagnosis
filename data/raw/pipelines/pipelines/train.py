import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

df = pd.read_csv("data/processed.csv")

X = df.drop("fault", axis=1)
y = df["fault"]

model = RandomForestClassifier()
model.fit(X, y)

joblib.dump(model, "model/model.pkl")
print("Model trained.")
