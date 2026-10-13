# WEBAPP
# 🛸 UFO Country Predictor

A machine learning web app that predicts the likely country of a UFO
sighting based on its latitude and longitude. Built with **scikit-learn**
and **Flask** as part of Microsoft's [ML for Beginners](https://github.com/microsoft/ML-For-Beginners)
curriculum.

---

## 📖 Overview

This project trains a **Logistic Regression** classifier on historical UFO
sighting data and exposes it through a simple Flask web interface. Enter a
latitude and longitude, and the app returns the most likely country where
that sighting was reported.

---

## 📁 Project Structure
WEBAPP/
│
├── .gitignore                  # Files Git should ignore (.venv, __pycache__, etc.)
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
├── LICENSE                     # (optional) open-source license
│
├── app.py                      # Flask web server — entry point
├── ufo-model.pkl               # Trained scikit-learn model (pickle)
├── ufo-countries.pkl           # Fitted LabelEncoder for country names (pickle)
│
├── templates/                  # HTML files served by Flask
│   └── index.html              # Main UI page
│
├── static/                     # (optional) CSS / JS / images
│   ├── style.css
│   └── logo.png
│
├── data/
│   └── ufos.csv                # Raw UFO sightings dataset
│
└── notebooks/                  # (optional) Jupyter notebooks for exploration
    └── training.ipynb          # Data cleaning + model training
