import joblib
import uvicorn
import numpy as np
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(debug=True) # initialize


class CarData(BaseModel):
    symboling: float
    normalized_losses: float
    make: float
    fuel_type: float
    aspiration: float
    num_of_doors: float
    body_style: float
    drive_wheels: float
    engine_location: float
    wheel_base: float
    length: float
    width: float
    height: float
    curb_weight: float
    engine_type: float
    num_of_cylinders: float
    engine_size: float
    fuel_system: float
    bore: float
    stroke: float
    compression_ratio: float
    horsepower: float
    peak_rpm: float
    city_mpg: float
    highway_mpg: float


# Routes
@app.get('/')
def home():
    return 'Welcome in Car Pricing App'

@app.post('/predict')
def predict(new_data: CarData):
    """TO DO : mettre un schema pydantic ou une dataclass pour les données + methode post au lieu de get."""
    try:
        print(new_data)
        inputs = [new_data.symboling,
                    new_data.normalized_losses,
                    new_data.make,
                    new_data.fuel_type,
                    new_data.aspiration,
                    new_data.num_of_doors,
                    new_data.body_style,
                    new_data.drive_wheels,
                    new_data.engine_location,
                    new_data.wheel_base,
                    new_data.length,
                    new_data.width,
                    new_data.height,
                    new_data.curb_weight,
                    new_data.engine_type,
                    new_data.num_of_cylinders,
                    new_data.engine_size,
                    new_data.fuel_system,
                    new_data.bore,
                    new_data.stroke,
                    new_data.compression_ratio,
                    new_data.horsepower,
                    new_data.peak_rpm,
                    new_data.city_mpg,
                    new_data.highway_mpg
                    ]
        inputs = np.reshape(inputs, (1,-1))
        model = joblib.load("./models_backup/final_model.joblib", 'r')
        makeprediction = model.predict(inputs)
        output = round(makeprediction[0],2)

        return {f'The right price for this car is : {output}'}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erreur_predict :: {e}")

if __name__ == '__main__':
    uvicorn.run(app)
    # uvicorn fast_api_pricing_voitures:app --reload   to reload after a modif  
    # np.reshape(array, (1, -1)) : transforme une liste en 2d array pour le model input
    # (-1, 1) transforme en 1 feature