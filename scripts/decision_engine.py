import os
import pickle
from scripts.data_collection import collect_data

def load_model():
    with open('../models/trained_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

def make_decision(data):
    model = load_model()
    decision = model.predict([data])
    return decision

if __name__ == "__main__":
    data = collect_data('sandbox-iosxe-latest-1.cisco.com', 'developer', 'C1sco12345')
    decision = make_decision(data)
    print(f"Decision: {decision}")
