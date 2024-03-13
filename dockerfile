ARG VERSION_PY=3.9.13
FROM python:$VERSION_PY
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
# Exposer le port pour l'application fastapi
EXPOSE 80
# Exposer le port pour l'application streamlit
EXPOSE 81
# Commande pour démar
# Vous pouvez utiliser un script shell qui démarre vos applications en arrière-plan
# al convention linux veut que l'on utilise le répertoire /usr/local/bin/ pour éxécuter des scripts sous unix/linux
COPY start.sh /usr/local/bin/start.sh
RUN chmod +x /usr/local/bin/start.sh
CMD ["/usr/local/bin/start.sh"]

