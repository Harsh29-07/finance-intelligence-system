from sklearn.ensemble import IsolationForest

def detect_anomalies(df):
    
    model = IsolationForest(
        contamination=0.03,
        random_state=42
    )
    
    df['anomaly'] = model.fit_predict(df[['Amount']])
    
    return df