from flask import Flask, request, jsonify
from ml_model import ChurnModel

app = Flask(__name__)
cmodel = ChurnModel()

@app.route('/')
def index():
    return jsonify({"message": "API v1.0"}), 200

@app.route('/churn', methods=["POST"])
def predict_churn():
    try:
        data = request.json

        # Check if required parameters are present
        if "age" not in data or "tenure" not in data:
            return jsonify({"error": "Missing 'age' or 'tenure' parameter"}), 400
        
        age = data["age"]
        tenure = data["tenure"]

        # Validate input values (must be positive numbers)
        if not isinstance(age, (int, float)) or age < 0:
            return jsonify({"error": "Invalid 'age' value. Must be a positive number."}), 400
        if not isinstance(tenure, (int, float)) or tenure < 0:
            return jsonify({"error": "Invalid 'tenure' value. Must be a positive number."}), 400

        # Validation: tenure cannot be greater than age
        if tenure > age:
            return jsonify({"error": "'tenure' cannot be greater than 'age'"}), 400

        # Make churn prediction
        churn_result = cmodel.predict(age, tenure)

        return jsonify(churn_result), 200

    except Exception as error:
        # Return error response in case of an exception
        return jsonify({"error": str(error)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

