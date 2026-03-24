import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def train_model():
    df = pd.read_csv("data/sample_data.csv")
    
    X = df.drop("label", axis=1)
    y = df["label"]
    
    model = RandomForestClassifier()
    model.fit(X, y)
    
    return model
