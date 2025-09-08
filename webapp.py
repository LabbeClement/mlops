#Level 0 (on your local machine) 
from turtle import st
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

# 1. Connect via SSH to the provided machine (ubuntu@20.54.250.141) password: Supermotdepasse!42.


# 2. Create a folder with your initial (td for Tom dupont for isntance)
# 3. Using scp or git clone, deploy your code on a remote machine (provided) in your folder
# 4. Launch your web service on the remote machine
# 5. Verify that you and a colleague can access your web service and get predictions