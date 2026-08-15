# TalknLock Marketing Intelligence

## Project Overview

TalknLock Marketing Intelligence is a machine learning project for analyzing marketing data and predicting marketing performance scores. The project includes data preprocessing, exploratory analysis, machine learning model training, model evaluation, and a Streamlit prototype.

## Project Workflow

Marketing Data
↓
Data Loading
↓
Data Preprocessing
↓
Exploratory Data Analysis
↓
Feature Preparation
↓
Model Training
↓
Model Evaluation
↓
Random Forest Model
↓
Streamlit Prototype

## Dataset

The project uses a synthetic marketing dataset containing marketing-related features and a performance score used as the prediction target.

The dataset is available in:

`data/synthetic_marketing_data_fixed.csv`

## Data Processing

The notebook performs the required data preparation and preprocessing steps before model training. These steps include loading the dataset, examining the data, preparing features and target variables, and splitting the data for model training and evaluation.

## Machine Learning Models

Two regression models were evaluated:

* Linear Regression
* Random Forest Regressor

The models were evaluated using:

* Mean Absolute Error (MAE)
* Root Mean Squared Error (RMSE)
* R² Score

## Model Evaluation

| Model             |    MAE |   RMSE |    R² |
| ----------------- | -----: | -----: | ----: |
| Linear Regression | 10.336 | 13.528 | 0.247 |
| Random Forest     | 10.218 | 13.295 | 0.273 |

Random Forest performed better than Linear Regression on the evaluation dataset, achieving the lowest MAE and RMSE and the highest R² score.

The final Random Forest model is saved in:

`models/performance_model.pkl`

## Project Structure

```text
talknlock-marketing-intelligence/
│
├── app/
│   └── streamlit_app.py
│
├── data/
│   └── synthetic_marketing_data_fixed.csv
│
├── models/
│   └── performance_model.pkl
│
├── notebooks/
│   ├── README.md
│   └── marketing_intelligence.ipynb
│
├── requirements.txt
└── README.md
```

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Streamlit
* Google Colab
* GitHub

## Running the Project

Clone the repository and install the required dependencies:

```bash
pip install -r requirements.txt
```

To run the Streamlit prototype:

```bash
streamlit run app/streamlit_app.py
```

## Files

* `notebooks/marketing_intelligence.ipynb` — data analysis, preprocessing, model training, and evaluation.
* `data/synthetic_marketing_data_fixed.csv` — project dataset.
* `models/performance_model.pkl` — trained Random Forest model.
* `app/streamlit_app.py` — Streamlit prototype.
* `requirements.txt` — Python dependencies.
