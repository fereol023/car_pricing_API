#!/bin/bash
# Démarrer fastapi sur le port 80
uvicorn fastapi_cars:app --host 0.0.0.0 --port 80 &
# et streamlit sur le port 81
streamlit run --server.port 81 /app/streamlit_cars.py &
# Empêcher le conteneur de se terminer immédiatement (seulement si nécessaire)
wait