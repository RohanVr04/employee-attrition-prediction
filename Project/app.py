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
    probability = model.predict_proba([features])[0][1]

    if prediction == 1:
        result = "High Attrition Risk"
    else:
        result = "Low Attrition Risk"

    return render_template(
        'result.html',
        prediction_text=result,
        probability=round(probability*100,2)
    )

app.run()
    