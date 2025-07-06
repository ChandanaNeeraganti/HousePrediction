# 🏠 Boston Housing Price Prediction

A Flask-based machine learning web app that predicts house prices based on various neighborhood and housing features from the Boston Housing dataset.

---

## 📌 Features

✅ Predicts median house price (`medv`) using 13 input features  
✅ Interactive UI to input features and get predictions  
✅ REST API endpoint for programmatic access  
✅ Trained using `Random Forest` from `scikit-learn`  
✅ Deployable to platforms like **Render**, **Heroku**, or any VPS

---

## 🧠 Machine Learning Model

This app uses a **Linear Regression** model trained on the following features:

- `rm` – Average number of rooms per dwelling  
- `age` – Proportion of owner-occupied units built prior to 1940  
- `ptratio` – Pupil-teacher ratio by town  
- `lstat` – % lower status of the population  
- `b` – 1000(Bk - 0.63)^2 where Bk is the proportion of Black people by town  
- `tax` – Property tax rate per $10,000  
- `rad` – Index of accessibility to radial highways  
- `dis` – Weighted distances to five Boston employment centers  
- `crim` – Per capita crime rate by town  
- `zn` – Proportion of residential land zoned for lots over 25,000 sq. ft.  
- `indus` – Proportion of non-retail business acres per town  
- `nox` – Nitric oxide concentration  
- `chas` – Charles River dummy variable (1 if tract bounds river; 0 otherwise)

---

## 🚀 Live Demo

> You can deploy the app to Render and link it here:
> https://dashboard.render.com/web/new

---

## 📁 Folder Structure

house_prediction/
├── app.py
├── BostonHousing.csv
├── model.pkl
├── requirements.txt
├── templates/
│ └── form.html


---

## 🖥️ Local Setup Instructions

1. **Clone the repo**  
```bash
git clone https://github.com/your-username/house_prediction.git
cd house_prediction

## install dependies
pip install -r requirements.txt

---

## run app
python app.py

---

## Open browser
Go to http://127.0.0.1:5000


