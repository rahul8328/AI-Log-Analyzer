from sklearn.ensemble import IsolationForest

def detect_anomalies(data):
    model = IsolationForest(contamination=0.3, random_state=42)
    data["anomaly"] = model.fit_predict(data[["attempt"]])
    return data