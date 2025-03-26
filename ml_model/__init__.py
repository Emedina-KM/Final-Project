import joblib
import numpy as np
import sklearn
import os

class ChurnModel: 
    def __init__(self):
        model_path = os.path.dirname(__file__)
        self.model = joblib.load(os.path.join(model_path, "churn_model.pkl"))
        self.scaler_x = joblib.load(os.path.join(model_path, "scaler_x.pkl"))

    def predict(self, age):
        """
        Realiza la predicción de churn basada en la edad.

        Parámetros:
        - age (int o float): Edad de la persona.

        Retorna:
        - Diccionario con la predicción y la probabilidad de churn.
        """
        # Escalar la edad antes de predecir
        age_scaled = self.scaler_x.transform(np.array([age]).reshape(-1, 1))
        
        # Obtener la probabilidad de churn
        churn_probability = self.model.predict_proba(age_scaled)[:, 1][0]  # Probabilidad de churn

        # Obtener la predicción final (0 = No Churn, 1 = Churn)
        churn_prediction = self.model.predict(age_scaled)[0]

        return {
            "age": age,
            "prediction": "Churn" if churn_prediction == 1 else "Not Churn",
            "probability": round(churn_probability, 2)
        }