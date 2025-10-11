#Choisir une image de base légère avec python
FROM python:3.13-slim

#Définir le répertoire de travail dans le conteneur
WORKDIR /app

#Copier le contenu du projet local dans le conteneur
COPY . /app

#Installer les dépendances du projet
RUN pip install --no-cache-dir -r requirements.txt

CMD ["Python", "main.py"]