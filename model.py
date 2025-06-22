import pandas as pd
from sklearn.ensemble import IsolationForest

def train_isolation_forest(data, contamination=0.05):
    model = IsolationForest(contamination=contamination, random_state=42)
    model.fit(data)
    return model

def predict_anomalies(model, data):
    preds = model.predict(data)
    data["anomaly"] = preds
    data["anomaly"] = data["anomaly"].map({1: "Normal", -1: "Anomaly"})
    return data