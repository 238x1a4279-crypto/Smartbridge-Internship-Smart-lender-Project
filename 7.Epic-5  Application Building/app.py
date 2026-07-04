import pickle
from flask import Flask, render_template, request

app = Flask(__name__)

# Load trained model
with open("decision_tree_model.pkl", "rb") as f:
    model = pickle.load(f)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/predict")
def predict():
    return render_template("predict.html")


@app.route("/submit", methods=["POST"])
def submit():
    try:
        # Take input in correct order
        input_feature = [
            int(request.form["Gender"]),
            int(request.form["Married"]),
            int(request.form["Dependents"]),
            int(request.form["Education"]),
            int(request.form["Self_Employed"]),
            float(request.form["ApplicantIncome"]),
            float(request.form["CoapplicantIncome"]),
            float(request.form["LoanAmount"]),
            float(request.form["Loan_Amount_Term"]),
            int(request.form["Credit_History"]),
            int(request.form["Property_Area"])
        ]

        # Predict
        prediction = model.predict([input_feature])[0]

        # Convert output
        result = "✅ Loan Approved" if prediction == 1 else "❌ Loan Not Approved"

        return render_template("result.html", result=result)

    except Exception as e:
        return f"Error occurred: {str(e)}"


if __name__ == "__main__":
    app.run(debug=True)