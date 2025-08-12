# House Price Prediction Using Flask & Linear Regression

A simple Flask web app that predicts house prices using a trained Linear Regression model.

---

##  Overview

This project loads a dataset (`Housing.csv`), trains a Linear Regression model on features like `area`, `bedrooms`, `bathrooms`, `stories`, `parking`, `mainroad`, and `airconditioning`, and exposes a web interface to input feature values and get price predictions.

---

##  Features

- Dataset preprocessing: encoding categorical variables (Yes/No → 1/0), scaling features using `StandardScaler`.
- Model training with `sklearn`'s `LinearRegression`.
- Web interface built with Flask:
  - Input form for feature values.
  - Outputs styled prediction results.
- Includes a Docker-friendly `render.yaml` for easy deployment, plus `requirements.txt` and `model.pkl`/`scaler.pkl`.

---

##  Project Structure

```
House_Price_Prediction/
│
├── app.py
├── Housing.csv
├── model.pkl
├── scaler.pkl
├── requirements.txt
├── render.yaml
├── House_price.ipynb
└── templates/
    └── index.html
```

---

##  Setup & Usage

1. **Clone the repo**  
   ```bash
   git clone https://github.com/AbikshaaDevi/House_Price_Prediction.git
   cd House_Price_Prediction
   ```

2. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app locally**  
   ```bash
   python app.py
   ```
   Then open your browser and go to `http://127.0.0.1:5000/`.

4. **Make a prediction**  
   Enter values for:
   - Area (sq.ft)
   - Bedrooms
   - Bathrooms
   - Stories
   - Parking
   - Mainroad (yes/no)
   - Airconditioning (yes/no)

   The app will return the predicted price in rupees.

---

##  Deployment

You can deploy this app on platforms like Render or Heroku. The included `render.yaml` makes deployment to Render straightforward. Alternatively, containerize with Docker.

---

##  About the Author

This project was created by **Abikshaa Devi** as a straightforward demonstration of combining ML with web development.

---

##  Contribution

Feel free to:
- Add model improvement (e.g., Ridge, Lasso, or ensemble methods)
- Enhance UI/UX or add responsive design
- Expand validations for form inputs

---

##  License

This project is open source—feel free to use it freely.
