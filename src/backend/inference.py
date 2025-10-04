import pandas as pd
import random

def predict_exoplanet(filepath):
    """
    Simple placeholder for ExoDiscover.
    Reads 'disposition' column and randomly selects one if multiple rows.
    """
    df = pd.read_csv(filepath)
    if "disposition" in df.columns:
        # randomly select one disposition as prediction
        prediction = random.choice(df['disposition'].tolist())
        confidence = round(random.uniform(0.7, 0.99), 2)
        return prediction, confidence
    return "CANDIDATE", 0.85
