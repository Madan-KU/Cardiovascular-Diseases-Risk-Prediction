import os
import pickle
import pandas as pd
from flask import Flask, flash, request, render_template, send_from_directory, redirect, url_for
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier

# Constants
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(CURRENT_DIR, 'models', 'best_model_rf_bayes.pkl')
SCALER_PATH = os.path.join(CURRENT_DIR, 'scaler', 'scaler.pkl')

# Flask application setup
application = Flask(__name__, static_folder='app/static', template_folder='app/templates')

# Load model and scaler
with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

with open(SCALER_PATH, 'rb') as file:
    scaler = pickle.load(file)

# Routes
@application.route('/')
def home():
    print('Accessing the home route...')
    return render_template("Predict.html")

@application.route('/admin')
def admin():
    print('Accessing the admin route...')
    return redirect(url_for("home"))

@application.route('/submit', methods=['POST'])
def submit():
    print('Receiving form data...')
    if request.method == 'POST':
        form_data = request.form
        print('Form data received:', form_data)
        print('Preprocessing input data...')
        input_data = preprocess_input(form_data)
        print('Making predictions...')
        prediction = model.predict(input_data)

    if prediction[0] > 0.5:
        result = "Positive for Heart Disease"
        print('Result:', result)
        image_path = 'static/positive.png'
    else:
        result = "Negative for Heart Disease"
        print('Result:', result)
        image_path = 'static/negative.png'

    return render_template("Predict.html", prediction=result, result_image=image_path)



def preprocess_input(form_data):
    print('Starting data preprocessing...')
    
    # Fields
    fields = [
        'General_Health_Excellent', 'General_Health_Fair', 'General_Health_Good', 'General_Health_Poor',
        'General_Health_Very Good', 'Checkup_5 or more years ago', 'Checkup_Never', 
        'Checkup_Within the past 2 years', 'Checkup_Within the past 5 years', 'Checkup_Within the past year',
        'Exercise_No', 'Exercise_Yes', 'Skin_Cancer_No', 'Skin_Cancer_Yes', 'Other_Cancer_No', 'Other_Cancer_Yes', 
        'Depression_No', 'Depression_Yes', 'Diabetes_No', 'Diabetes_No, pre-diabetes or borderline diabetes', 
        'Diabetes_Yes', 'Diabetes_Yes, but female told only during pregnancy', 'Arthritis_No', 'Arthritis_Yes', 
        'Sex_Female', 'Sex_Male', 'Age_Category_18-24', 'Age_Category_25-29', 'Age_Category_30-34', 
        'Age_Category_35-39', 'Age_Category_40-44', 'Age_Category_45-49', 'Age_Category_50-54', 'Age_Category_55-59',
        'Age_Category_60-64', 'Age_Category_65-69', 'Age_Category_70-74', 'Age_Category_75-79', 'Age_Category_80+',
        'Smoking_History_No', 'Smoking_History_Yes', 'Height_(cm)', 'Weight_(kg)', 'BMI', 'Alcohol_Consumption',
        'Fruit_Consumption', 'Green_Vegetables_Consumption', 'FriedPotato_Consumption'
    ]
    
    # Initialize DataFrame
    df = pd.DataFrame(columns=fields)
    df.loc[0] = 0

    # Numeric fields
    numeric_fields = ['Height_(cm)', 'Weight_(kg)', 'BMI', 'Alcohol_Consumption', 
                      'Fruit_Consumption', 'Green_Vegetables_Consumption', 'FriedPotato_Consumption']
    
    for field in numeric_fields:
        df.at[0, field] = float(form_data.get(field))
    
    # Categorical fields
    categorical_fields = ['General_Health', 'Checkup', 'Exercise', 'Heart_Disease', 'Skin_Cancer', 
          'Other_Cancer', 'Depression', 'Diabetes', 'Arthritis', 'Sex', 'Age_Category', 'Smoking_History']
    
    for field in categorical_fields:
        value = form_data.get(field)
        if value:
            df.at[0, value] = 1
    
    # Scaling numeric fields
    df[numeric_fields] = scaler.transform(df[numeric_fields])

    print(df.T, '\n')
    return df


if __name__ == '__main__':
    application.run(debug=True,host="0.0.0.0",port=5000)
