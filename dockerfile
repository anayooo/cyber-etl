# 1️⃣ Utiliser une image Python légère
FROM python:3.13-slim

# 2️⃣ Définir le répertoire de travail
WORKDIR /app

# 3️⃣ Copier uniquement les dépendances d'abord pour optimiser le cache
COPY requirements.txt .

# 4️⃣ Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copier tout le reste du projet dans l'image
COPY . .

# 6️⃣ Vérifier que les fichiers sont bien copiés
RUN ls -R /app/data || echo "⚠️ Dossier data manquant"

# 7️⃣ Définir la commande par défaut
CMD ["python", "main.py"]
