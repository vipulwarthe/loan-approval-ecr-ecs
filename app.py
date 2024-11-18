from flask import Flask, render_template, request
import pandas as pd
import pickle

# Create a Flask app instance
app = Flask(__name__)

# Load the pre-trained model (modify the path to your model file if needed)
model = pickle.load(open('notebook/random_forest_model.pkl', 'rb'))  # Your model file path here

# Load dataset (modify the path to the dataset)
data = pd.read_csv('notebook/LoanApprovalPrediction.csv')  # Modify with your actual file path

# Define the route for the landing page (index.html)
@app.route('/')
def index():
    return render_template('index.html')

# Define the route for the home page (home.html)
@app.route('/home')
def home():
    # You can pass the dataset or other necessary data to home.html if needed
    return render_template('home.html', data=data)

# Define the route for loan prediction (if you want to process input data)
@app.route('/predict', methods=['POST'])
def predict():
    # Get data from the form
    income = float(request.form['income'])
    loan_amount = float(request.form['loan_amount'])
    
    # Assuming the model uses income and loan_amount as features
    prediction = model.predict([[income, loan_amount]])

    # Return the prediction result to a new template (you can modify this part)
    if prediction == 1:
        result = "Loan Approved"
    else:
        result = "Loan Denied"
    
    return render_template('prediction_result.html', prediction=result)

# Run the app in debug mode
if __name__ == '__main__':
    app.run(debug=True)

