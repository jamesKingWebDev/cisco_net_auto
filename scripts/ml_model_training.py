import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

def train_model(data_path):
    data = pd.read_csv(data_path)
    X = data.drop('target', axis=1)
    y = data['target']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Storing the model
    with open('../models/trained_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    print("Trained model executed and saved successfully.")

if __name__ == "__main__":
    train_model('data/training_data.csv')
