from flask import Flask, render_template, request
import joblib

model = joblib.load('best_model2.pkl')

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():

    features = [
    float(request.form['OverTime']),
    float(request.form['StockOptionLevel']),
    float(request.form['JobLevel']),
    float(request.form['Department']),
    float(request.form['JobInvolvement']),
    float(request.form['BusinessTravel']),
    float(request.form['YearsInCurrentRole']),
    float(request.form['MaritalStatus']),
    float(request.form['EnvironmentSatisfaction']),
    float(request.form['PerformanceRating']),
    float(request.form['JobSatisfaction']),
    float(request.form['TotalWorkingYears']),
    float(request.form['WorkLifeBalance']),
    float(request.form['Age']),
    float(request.form['MonthlyIncome'])
]

    prediction = model.predict([features])[0]
    probabilities = model.predict_proba([features])[0]

    stay_probability = round(probabilities[0] * 100, 2)
    leave_probability = round(probabilities[1] * 100, 2)

    if prediction == 1:
        result = "High Attrition Risk"
        confidence = leave_probability
    else:
        result = "Low Attrition Risk"
        confidence = stay_probability

    return render_template(
        "result.html",
        prediction_text=result,
        confidence=confidence,
        stay_probability=stay_probability,
        leave_probability=leave_probability
    )

if __name__ == "__main__":
    app.run(debug=True)
    
