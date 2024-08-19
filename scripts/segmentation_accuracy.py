import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

def train_segmentation_model(data_path):
    data = pd.read_csv(data_path)
    X = data.drop('segment', axis=1)
    y = data['segment']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the model
    with open('../models/segmentation_model.pkl', 'wb') as f:
        pickle.dump(model, f)

    # Evaluate model accuracy
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy}")

    return accuracy

if __name__ == "__main__":
    accuracy = train_segmentation_model('data/data_segmentation.csv')