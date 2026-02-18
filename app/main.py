from fastapi import FastAPI
from pydantic import BaseModel # TODO: review pydantic
import random

app = FastAPI()

# /predict
class PredictionOut(BaseModel):
    prediction: str
    probability: float
    message: str=""


@app.get("/")
async def root(): # TODO: review async def
    return {"message": "Hello World"}

@app.get("/health") # TODO: expand on to reflect industry-standard practices
async def health_check():
    return {"status": "healthy"}

@app.post("/predict")
async def predict_coin_flip():
    result = random.choice(["Heads", "Tails"])
    prob = round(random.uniform(0.48, 0.52), 3) # fake 'confidence'
    return PredictionOut(
        prediction=result,
        probability=prob,
        message=f"The coin flip says: {result}!"
    )