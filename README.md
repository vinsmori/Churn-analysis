## 🚀 Churn Analysis with Machine Learning

Churn modeling using scikit-learn pipelines, ColumnTransformer, hyperparameter search, model persistence, and a real-time inference demo (Streamlit).

This project applies an end-to-end machine learning workflow to predict customer churn using the Telco Customer Churn dataset.
It includes data preprocessing, feature engineering, model training, evaluation, and deployment.


## 📁 Project Structure

```text
churn_analysis/
│
├── data/
│   ├── raw/            # Original dataset
│   └── processed/      # Cleaned / transformed data
│
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_feature_engineering.ipynb
│   ├── 03_model_training.ipynb
│   └── 04_explainability.ipynb
│
├── src/
│   ├── data_prep.py    # Data loading, cleaning, splitting
│   ├── training.py     # Pipelines, model training, hyperparameter search
│   ├── utils.py        # Helper functions (paths, etc.)
│
├── models/             # Saved models (joblib / pickle)
│
├── app/
│   └── app.py          # Streamlit demo for interactive predictions
│
└── README.md
```

## 🎯 Objectives

	•	Build a reproducible ML pipeline using scikit-learn
	•	Perform feature engineering for mixed numeric/categorical data
	•	Train and compare multiple models
	•	Apply hyperparameter tuning (RandomizedSearchCV / GridSearchCV)
	•	Interpret model decisions with feature importance / SHAP
	•	Deploy a simple Streamlit app for real-time churn prediction

    
## 🛠️ Tech Stack

	•	Python 3.x
	•	pandas, numpy
	•	scikit-learn
	•	matplotlib, seaborn
	•	joblib (model persistence)
	•	Streamlit (demo app)


## ▶️ How to Run

1. Create and activate the virtual environment
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
.venv\Scripts\Activate.ps1  # Windows

2. Install dependencies
pip install -r requirements.txt

3. Run notebooks
Inside the notebooks/ folder, open the .ipynb files with Jupyter or VS Code.


4. Run the Streamlit app (after training the model)
streamlit run app/app.py

## 📦 Dataset

This project uses the Telco Customer Churn dataset (publicly available on Kaggle).

Place it inside:
data/raw/

File name: 
Telco-Customer-Churn.csv

## 📈 Roadmap (to be completed)
	•	Complete exploratory data analysis (notebook 01)
	•	Build preprocessing and feature engineering pipeline
	•	Train baseline models
	•	Add hyperparameter tuning
	•	Add model explainability (SHAP)
	•	Deploy the real-time prediction Streamlit app
	•	Improve documentation & visualizations
	•	Add tests + CI (optional, future step)



## 🧑‍💻 Author

Vinícius Mori
Data Science & Machine Learning - Engineering Student (Télécom Paris / Paris Dauphine)