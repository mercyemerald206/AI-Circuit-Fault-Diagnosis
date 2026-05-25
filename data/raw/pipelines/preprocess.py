import pandas as pd

df = pd.read_csv("data/raw/fault_data.csv")

df["voltage_diff"] = df["Va"] - df["Vb"]
df["current_ratio"] = df["Ia"] / (df["Ib"] + 1e-6)

df["fault"] = df["fault"].astype("category").cat.codes

df.to_csv("data/processed.csv", index=False)
print("Preprocessing complete.")
