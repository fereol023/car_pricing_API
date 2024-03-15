import streamlit as st
import numpy as np
import joblib

st.title("Prédiction du prix d'une voiture en fonction de ses caractéristiques")
st.subheader("Application réalisée par Féréol")
st.markdown("*Cette application se base sur un modèle de machine learning pour estimer le prix d'une voiture selon les données du marché (au sens vague).*")


# definition d'une fonction d'inférence
# def inference(symboling, normalized_losses, wheel_base, length, width, height, curb_weight, engine_size, compression_ratio, horse_power, peak_rpm, city_mpg, highway_mpg) :
    
def inference(symboling, normalized_losses, make, fuel_type, aspiration,
              num_of_doors, body_style, drive_wheels, engine_location, wheel_base,
              length, width, height, curb_weight, engine_type, num_of_cylinders,
              engine_size, fuel_system, bore, stroke, compression_ratio,
              horsepower, peak_rpm, city_mpg, highway_mpg) :
    
    """
    Prends les caracteristiques de la voiture et renvoie le prix selon le modele de ML sauvegardé.
    """
    new_data = np.array([
        symboling, normalized_losses, make, fuel_type, aspiration, num_of_doors, body_style, drive_wheels, engine_location, wheel_base, 
        length, width, height, curb_weight, engine_type, num_of_cylinders, engine_size, fuel_system, bore, stroke, compression_ratio, 
        horse_power, peak_rpm, city_mpg, highway_mpg
    ])

    # chargement du modèle
    model = joblib.load("./models_backup/final_model.joblib", 'r')

    # prediction
    return model.predict(new_data.reshape(1, -1))

# features saisies par l'utilisateur
# données par défaut (valeurs médianes)
symboling = st.number_input(label='symboling:', min_value=0, value=3)
normalized_losses = st.number_input('normalized_losses', value=100)
make = st.number_input('make', value=11)
fuel_type = st.number_input('fuel_type', value=0)
aspiration = st.number_input('aspiration', value=0)
num_of_doors = st.number_input('num_of_doors', value=4)
body_style = st.number_input('body_style', value=2)
drive_wheels = st.number_input('drive_wheels', value=2)
engine_location = st.number_input('engine_location', value=1)
wheel_base = st.number_input('wheel_base', value=90)
length = st.number_input('length', value=150)
width = st.number_input('width', value=65)
height = st.number_input('height', value=50)
curb_weight = st.number_input('curb_weight', value=200)
engine_type = st.number_input('engine_type', value=3)
num_of_cylinders = st.number_input('wheel_base', value=4)
engine_size = st.number_input('engine_size', value=120)
fuel_system = st.number_input('fuel_system', value=1)
bore = st.number_input('bore', value=3.05)
stroke = st.number_input('stroke', value=3.35)
compression_ratio = st.number_input('compression_ratio', value=9)
horse_power = st.number_input('horse_power', value=110)
peak_rpm = st.number_input('peak_rpm', value=5200)
city_mpg = st.number_input('city_mpg', value=24)
highway_mpg = st.number_input('highway_mpg', value=30) 

# creation du bouton "predict" qui retourne la prediction
if st.button("Estimer le prix") :
    prediction = inference(
        symboling, normalized_losses, make, fuel_type, aspiration,
        num_of_doors, body_style, drive_wheels, engine_location, wheel_base,
        length, width, height, curb_weight, engine_type, num_of_cylinders,
        engine_size, fuel_system, bore, stroke, compression_ratio,
        horse_power, peak_rpm, city_mpg, highway_mpg
    )
    res = f"Le prix de cette voiture est : {round(prediction[0], 4)} $."
    st.success(res)









