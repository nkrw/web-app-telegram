import pickle
import numpy as np

# Charger le modèle ML
def load_model(model_path):
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model

# Faire une prédiction avec le modèle ML
def predict(model, data):
    data = np.array(data).reshape(1, -1)  # Adapter les données si nécessaire
    prediction = model.predict(data)
    return prediction