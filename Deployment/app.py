from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd


# Load the trained model
with open('D:\only projects\Machine learning projects\insurance_predictor\Deployment\gbr.pkl', 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract values from the form
    age = float(request.form['age'])
    sex = request.form['sex']
    bmi = float(request.form['bmi'])
    children = int(request.form['children'])
    smoker = request.form['smoker']
    region = request.form['region']

    # Create a dataframe with the input features
    input_data = pd.DataFrame({
        'age': [age],
        'sex_male': [1 if sex == 'male' else 0],
        'bmi': [bmi],
        'children': [children],
        'smoker_yes': [1 if smoker == 'yes' else 0],
        'region_northwest': [1 if region == 'northwest' else 0],
        'region_southeast': [1 if region == 'southeast' else 0],
        'region_southwest': [1 if region == 'southwest' else 0]
    })
    data_list = input_data.values.tolist()
    # Make prediction
    prediction = model.predict(np.array(data_list))

    return render_template('result.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)