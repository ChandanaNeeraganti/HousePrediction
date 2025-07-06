# HousePrediction
Using Random Forest Model
# 🏠 Boston Housing Price Prediction API

This project is a **machine learning web API** built using **Flask** that predicts house prices based on features from the Boston Housing dataset

## 🌐 Live Demo

🔗 [Visit Deployed App on Render](https://boston-housing-model-api.onrender.com)

## 🧠 Model Inputs

The model expects these 13 features:

| Feature    | Description                                                 |
|------------|-------------------------------------------------------------|
| `crim`     | Per capita crime rate by town                              |
| `zn`       | Proportion of residential land zoned for large lots        |
| `indus`    | Proportion of non-retail business acres                     |
| `chas`     | Charles River dummy variable (0 or 1)                       |
| `nox`      | Nitric oxide concentration                                  |
| `rm`       | Average number of rooms per dwelling                        |
| `age`      | Proportion of owner-occupied units built before 1940        |
| `dis`      | Weighted distances to employment centers                    |
| `rad`      | Accessibility to radial highways                            |
| `tax`      | Property-tax rate per $10,000                               |
| `ptratio`  | Pupil-teacher ratio by town                                 |
| `b`        | Racial composition factor                                   |
| `lstat`    | % of lower status of the population                         |

---

## 🔄 API Usage

### ▶️ POST `/predict`

#### 📤 Request Body (JSON):
```json
{
  "crim": 0.2,
  "zn": 0.0,
  "indus": 7.0,
  "chas": 0,
  "nox": 0.5,
  "rm": 6.2,
  "age": 45.0,
  "dis": 4.0,
  "rad": 4,
  "tax": 300,
  "ptratio": 15.5,
  "b": 390.0,
  "lstat": 12.5
}

{
  "prediction": 24.37
}



