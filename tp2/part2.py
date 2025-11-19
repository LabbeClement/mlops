from fastapi import FastAPI
import pandas as pd
from sklearn import datasets
from main import model_info, y_test
import mlflow.pyfunc

app = FastAPI()

# Load the model back for predictions as a generic Python Function model
loaded_model = mlflow.pyfunc.load_model(model_info.model_uri)


@app.post("/predict")
def predict(sepal_length: float, sepal_width: float, petal_length: float, petal_width: float):
    iris_feature_names = datasets.load_iris().feature_names
    input_df = pd.DataFrame([[sepal_length, sepal_width, petal_length, petal_width]], columns=iris_feature_names)
    prediction = loaded_model.predict(input_df)[0]
    return {"prediction": int(prediction)}

@app.post("/update-model")
def update_model(model_version: str):
    global loaded_model
    model_uri = f"models:/iris_model/{model_version}"
    loaded_model = mlflow.pyfunc.load_model(model_uri)
    return {"message": f"Model updated to version {model_version}"}