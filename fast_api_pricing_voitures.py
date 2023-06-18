import joblib
import uvicorn
from fastapi import FastAPI

app = FastAPI(debug=True)

@app.get('/')
def home():
    return {'text': 'Car Pricing Prediction Solution'}

if __name__ == '__main__':
    uvicorn.run(app)