import joblib
import numpy as np
import os

class ChurnModel: 
    #Initializes the ChurnModel class by loading the pre-trained model
    #and the scaler used for standardizing input features.

    def __init__(self):
        model_path = os.path.dirname(__file__)
        self.model = joblib.load(os.path.join(model_path, "churn_model.pkl"))
        self.scaler_x = joblib.load(os.path.join(model_path, "scaler_x.pkl"))

    # Predicts customer churn based on age and tenure.
    def predict(self, age, tenure):

        # Create a NumPy array with the input features (age and tenure).
        input_data = np.array([[age, tenure]])

        # Scale the input data using the preloaded scaler.
        input_scaled = self.scaler_x.transform(input_data)
        # Get the probability of churn.
        churn_probability = self.model.predict_proba(input_scaled)[:, 1][0]
        # Get the final churn prediction.
        churn_prediction = self.model.predict(input_scaled)[0]

        # Format the prediction result as a descriptive string.
        churn_prediction_result = (f"A person aged {age} with {tenure} years of tenure is predicted to "
                   f"{'Churn' if churn_prediction == 1 else 'Not Churn'}. "
                   f"(Probability: {churn_probability:.2f})")

        return churn_prediction_result
