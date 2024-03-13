### Application d'estimation du prix de voitures

04/04/23 - Ajout d'un ensemble de fonctionnalités dans la modélisation cf. [build_model_v2.ipynb] : 
- modèle principal RandomForestRegressors 
- Cross Validation avec GridSearchCV et RandomSearchCV : comparaison des résultats et du temps de traitement 
- pipeline de preprocessing (reste à intégrer au model final) : imputation + encodage des variables "object" 
- features importance - learning curve visualization

18/06/23 - scripts cf. streamlit_api_pricing_voitures.py et fast_api_pricing_voitures.py
13/03/24 - déploiement des 2 api web qui interfacent avec le modèle avec docker

- Estimation du prix de voitures selon leurs <b>caractéristiques techniques uniquement</b>.
- Rendu exposé sous forme de 2 applications web embarquées dans 1 même conteneur docker.
- Pour l'application ``streamlit``, utiliser le port 81 du conteneur `fereol023/p8_carpricing`. Par exemple :
  ```
      - docker run -it -p 8001:81 fereol023/p8_carpricing   
  ```

- Pour l'application ``fastapi``, utiliser le port 80 du conteneur `fereol023/p8_carpricing`. Par exemple :
  ```
      - docker run -it -p 8001:80 fereol023/p8_carpricing   
  ```
  
- L'image docker embarque les modèles de machine learning utilisés, pas les datasets, ni les scripts de train/validation.
