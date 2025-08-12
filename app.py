from flask import Flask, render_template, request
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

app = Flask(__name__)

# Load dataset
df = pd.read_csv("Housing.csv")

# Clean only needed columns
df['mainroad'] = df['mainroad'].str.strip().str.lower().map({'yes': 1, 'no': 0})
df['airconditioning'] = df['airconditioning'].str.strip().str.lower().map({'yes': 1, 'no': 0})

# Select relevant features
features = ['area', 'bedrooms', 'bathrooms', 'stories', 'parking', 'mainroad', 'airconditioning']
X = df[features]
y = df['price']

# Standardize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train model
model = LinearRegression()
model.fit(X_scaled, y)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        area = float(request.form['area'])
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        stories = int(request.form['stories'])
        parking = int(request.form['parking'])
        mainroad = 1 if request.form['mainroad'].lower() == 'yes' else 0
        airconditioning = 1 if request.form['airconditioning'].lower() == 'yes' else 0

        input_data = np.array([[area, bedrooms, bathrooms, stories, parking, mainroad, airconditioning]])
        input_scaled = scaler.transform(input_data)
        prediction = model.predict(input_scaled)

        return f"""
        <body style="background-color: #d3e0ea; font-family: sans-serif;">
            <div style="text-align:center; margin-top:100px;">
                <h2 style="font-size:28px;">Predicted House Price:</h2>
                <p style="font-size:24px; font-weight:bold;">₹ {round(prediction[0], 2)}</p>
                <a href="/" style="font-size:18px;">Try another prediction</a>
            </div>
        </body>
        """
    except Exception as e:
        return f"<h3>Error: {str(e)}</h3>"

if __name__ == '__main__':
    app.run(debug=True)
