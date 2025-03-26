import joblib
import numpy as np
import os

class ChurnModel: 
    def __init__(self):
        model_path = os.path.dirname(__file__)
        self.model = joblib.load(os.path.join(model_path, "churn_model.pkl"))
        self.scaler_x = joblib.load(os.path.join(model_path, "scaler_x.pkl"))

    def predict(self, age, tenure):

        input_data = np.array([[age, tenure]])

        input_scaled = self.scaler_x.transform(input_data)
        churn_probability = self.model.predict_proba(input_scaled)[:, 1][0]  
        churn_prediction = self.model.predict(input_scaled)[0]

        churn_prediction_result = (f"A person aged {age} with {tenure} years of tenure is predicted to "
                   f"{'Churn' if churn_prediction == 1 else 'Not Churn'}. "
                   f"(Probability: {churn_probability:.2f})")

        return churn_prediction_result
