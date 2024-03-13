import joblib
import numpy as np
import uvicorn
from fastapi import FastAPI

app = FastAPI(debug=True) # initialize

@app.get('/')
def home():
    return {'Msg': 'Car Pricing Prediction Solution'}

@app.get('/predict')
def predict(symboling: float, normalized_losses: float, make: float, fuel_type: float, aspiration: float, num_of_doors: float, body_style: float, drive_wheels: float, engine_location: float, wheel_base: float, 
        length: float, width: float, height: float, curb_weight: float, engine_type: float, num_of_cylinders: float, engine_size: float, fuel_system: float, bore: float, stroke: float, compression_ratio: float, 
        horsepower: float, peak_rpm: float, city_mpg: float, highway_mpg: float):
    """TO DO : mettre un schema pydantic ou une dataclass pour les données + methode post au lieu de get."""


    new_data = np.reshape([
        symboling, normalized_losses, make, fuel_type, aspiration, num_of_doors, body_style, drive_wheels, engine_location, wheel_base, 
        length, width, height, curb_weight, engine_type, num_of_cylinders, engine_size, fuel_system, bore, stroke, compression_ratio, 
        horsepower, peak_rpm, city_mpg, highway_mpg
    ], (1,-1))

    model = joblib.load("./models_backup/final_model.joblib", 'r')
    makeprediction = model.predict(new_data)
    output = round(makeprediction[0],2)

    return {f'Sell your car for {output}'}

if __name__ == '__main__':
    uvicorn.run(app)
    # uvicorn fast_api_pricing_voitures:app --reload   to reload after a modif  
    # np.reshape(array, (1, -1)) : transforme une liste en 2d array pour le model input
    # (-1, 1) transforme en 1 feature