import joblib

model = joblib.load("./models_backup/final_model.joblib")#, 'r')
#model = joblib.load("./models_backup/rcv_best_model.joblib")
print(model.feature_names_in_)