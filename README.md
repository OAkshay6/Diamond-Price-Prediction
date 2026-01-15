# Diamond Price Prediction

## Project Overview
This project is an end-to-end machine learning application designed to **predict diamond prices** based on their physical and quality attributes.  
It covers the complete data science lifecycle, including **Exploratory Data Analysis (EDA), model training, hyperparameter tuning, and deployment using **Streamlit**.

The goal is to build an accurate, robust, and deployable price prediction system that can be used in real-world scenarios.

---

## Dataset Description
The dataset contains information about diamonds, including:

- **Carat** – Weight of the diamond  
- **Cut** – Quality of the cut (Fair, Good, Very Good, Premium, Ideal)  
- **Color** – Color grade (D = best, J = worst)  
- **Clarity** – Clarity grade (I1 = worst, IF = best)  
- **Depth (%)** – Total depth percentage  
- **Table (%)** – Width of the top of the diamond  
- **Dimensions (x, y, z)** – Physical dimensions in millimeters  
- **Price** – Diamond price (target variable)

---

## Exploratory Data Analysis (EDA)
EDA was performed to understand data distributions, detect anomalies, and analyze relationships.

Key EDA steps:
- Distribution analysis of numerical and categorical features
- Detection of invalid entries (e.g., zero values in dimensions)
- Analysis of price variation across cut, color, and clarity
- Correlation analysis between numerical features

---

## Model Development
The following regression models were trained and evaluated:

- Linear Regression  
- K-Nearest Neighbors (KNN)  
- Decision Tree Regression  
- Random Forest Regression  

### Evaluation Metrics Used
- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

---

## Model Comparison & Selection
After evaluating all models:

- **Random Forest Regression** achieved the best performance
- Lowest MAE and RMSE
- Highest test R² score (0.98)
- Better generalization compared to Decision Tree

---

## Hyperparameter Tuning & Pipeline
- Implemented a **Pipeline** combining preprocessing and modeling
- Used **ColumnTransformer** for numerical and categorical preprocessing
- Applied **RandomizedSearchCV with 5-fold cross-validation**
- Reduced overfitting and improved model stability

---

## Deployment
The final tuned model was deployed using **Streamlit**.

### Deployment Features
- Interactive UI for user input
- Real-time price prediction
- Model loaded via Pickle
- End-to-end pipeline ensures consistent preprocessing

---

## How to Run the Project

1. Open Anaconda Prompt
2. Navigate to the project directory and change the current directory to the location where the folder Project 2 - Diamond Dataset is saved:
> cd path_to/Project 2 - Diamond Dataset

3. Run the Streamlit application

> streamlit run app.py

4. Access the application

- The command will automatically open the app in your default web browser.
- If it does not open automatically, copy and paste the provided local URL into the browser.

5. Make predictions

- Enter the required input values using the sliders or input ranges.
- Submit the inputs to predict the output based on the trained model.

**Notes** 

Ensure Streamlit is installed:

> pip install streamlit


Activate the correct environment before running the app.

Keep app.py, model files, and supporting scripts in the same directory.

## Author
Akshaykumar Obuladinne 
GitHub: https://github.com/OAkshay6

