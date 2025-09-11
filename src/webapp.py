#Level 0 (on your local machine) 
from fastapi import FastAPI
import uvicorn
app = FastAPI()

@app.get("/predict")
async def root():
    return {"y_pred": 2}

@app.post("/predict")
def predict(size: float = 0, bedrooms: int = 0, garden: int = 0):
    import joblib
    model = joblib.load("regression.joblib")
    prediction = model.predict([[size, bedrooms, garden]])
    return {"y_pred": prediction[0]}

uvicorn.run(app, host="0.0.0.0", port=8963)