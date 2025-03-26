from flask import Flask, request, jsonify
from ml_model import ChurnModel

app = Flask(__name__)
cmodel = ChurnModel()  # Se carga solo una vez

@app.route('/')
def index():
    return jsonify({"message": "API v1.0"}), 200

@app.route('/churn', methods=["POST"])
def predict_churn():
    try:
        data = request.json
        if "age" not in data:
            return jsonify({"error": "Missing 'age' parameter"}), 400
        
        age = data["age"]
        if not isinstance(age, (int, float)) or age < 0:
            return jsonify({"error": "Invalid 'age' value. Must be a positive number."}), 400

        churn = cmodel.predict(age)

        return jsonify({"age": age, "churn": churn}), 200

    except Exception as error:
        return jsonify({"error": str(error)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)

