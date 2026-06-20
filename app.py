from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():

    return {
        "project":
        "HealthLens Multimodal Diagnosis System"
    }

@app.route("/predict", methods=["POST"])
def predict():

    patient_age = request.form["age"]

    result = {
        "prediction":
        "Low Risk",
        "confidence":
        "91%"
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)