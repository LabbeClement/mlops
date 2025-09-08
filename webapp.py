#Level 0 (on your local machine) 
from fastapi import FastAPI
import joblib

app = FastAPI()
@app.post("/predict")
def predict(size: float = 0, bedrooms: int = 0, garden: int = 0):
    import joblib
    model = joblib.load("regression.joblib")
    prediction = model.predict([[size, bedrooms, garden]])
    return {"y_pred": prediction[0]}

#Level 0.5 (on a remote machine)

# 4. Launch your web service on the remote machine
# 5. Verify that you and a colleague can access your web service and get predictions