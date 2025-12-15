# Overview
This project is an AI-based Learning Agent designed to analyze historical seismic data, verify data quality, and predict earthquake risks. It utilizes Machine Learning (Random Forest) to forecast earthquake probability and magnitude for specific regions over a 7-day window.

The system includes a Data Verification Pipeline to ensure dataset integrity and a Streamlit Dashboard for interactive visualization of seismic trends, magnitude distributions, and risk probability metrics.

# Features
### 1. Data Verification & Exploration (EDA)
Automated Quality Checks: Validates column existence, data types, and value ranges (e.g., Latitude [-90, 90]).

Statistical Analysis: Generates summary statistics for magnitude, depth, and frequency.

Missing Value Handling: Detects and reports null values to ensure data readiness.

Categorization: Classifies earthquakes into categories: Minor (<3), Moderate (3-5), Strong (5-7), Major (>7).

### 2. Predictive Modeling
Risk Forecasting: Calculates a 7-Day Earthquake Risk Probability for selected regions.

Magnitude Prediction: Uses Random Forest Regression to predict potential earthquake magnitude based on geological features (Latitude, Longitude, Depth, Time).

Model Evaluation: Tracks accuracy using Mean Squared Error (MSE) and Root Mean Squared Error (RMSE).

### 3. Interactive Dashboard
Country Selector: Filter analysis by specific countries or regions (e.g., Japan, Indonesia, USA).

Dynamic Visualizations:

Magnitude Distribution Histograms

Depth vs. Magnitude Correlation Scatter Plots

Geospatial Maps of Epicenters

Risk Forecast Line Charts

# 🛠️ Tech Stack
Language: Python

Data Manipulation: Pandas, NumPy

Visualization: Matplotlib, Seaborn

Machine Learning: Scikit-Learn (Random Forest Regressor)

Frontend/Dashboard: Streamlit

Notebooks: Jupyter / Google Colab

# 📂 Dataset Structure
The model expects a CSV file (e.g., database.csv or earthquake.csv) with the following core columns:

Column	Description
Date	Date of the event (YYYY-MM-DD)
Time	Time of the event (UTC)
Latitude	Decimal degrees latitude
Longitude	Decimal degrees longitude
Depth	Depth of the event in kilometers
Magnitude	Richter scale magnitude
Place	Description of the region (e.g., "12km SE of Tokyo")

Export to Sheets

# Visualizations
The project generates several key insights:

Magnitude Distribution: Analysis of the frequency of different earthquake intensities.

7-Day Risk Forecast: A probabilistic trend line showing the likelihood of seismic activity in the coming week.

Depth Analysis: Verifies correlation between earthquake depth and magnitude impact.

# Installation & Usage
1. Clone the Repository
Bash

git clone https://github.com/Abdrash12/earthquake-prediction-ai.git
cd earthquake-prediction-ai
2. Install Dependencies
Bash

pip install pandas numpy matplotlib seaborn scikit-learn streamlit
3. Run the Dashboard
To launch the interactive frontend:

Bash

streamlit run app.py
4. Run the EDA Notebook
To view the data verification and exploration steps:

Bash

jupyter notebook Earthquauke_Prediction.ipynb
# 📈 Project Goals
Data Integrity: Create a robust pipeline that rejects invalid seismic data before training.

Accessibility: Make complex earthquake risk metrics understandable through a simple UI.

Accuracy: Minimize MSE in magnitude prediction to provide reliable early warnings.

# 🤝 Contributing
Contributions are welcome! Please fork the repository and create a pull request with your features or fixes.

# 📜 License
This project is licensed under the MIT License.
