# main.py
import os
from dotenv import load_dotenv
import pandas as pd
from etl.extract import extract_csv, extract_json, extract_api, extract_db
from etl.transform import transform_data
from etl.load import load_csv


# -------------------------------------------------
# 1️⃣ Charger les variables d'environnement
# -------------------------------------------------
load_dotenv()
api_key = "2feaaf26759da77632157d11acb8edb345ebd759094abfdad3679bdee1d26a484866bf975dbe7820"

# -------------------------------------------------
# 2️⃣ Définir les fichiers et paramètres
# -------------------------------------------------
# Fichiers locaux
csv_file = r"C:\Users\HP\Desktop\Python\Cyber ETL\cyber-etl\data\raw\logs_auth.csv"
json_file = r"C:\Users\HP\Desktop\Python\Cyber ETL\cyber-etl\data\raw\malware.json"

# API AbuseIPDB
api_url = "https://api.abuseipdb.com/api/v2/check?ipAddress=8.8.8.8"
headers = {
    "Key": api_key,
    "Accept": "application/json"
}

# -------------------------------------------------
# 3️⃣ Extraire les données
# -------------------------------------------------

#a) CSV
try:
    df_logs = extract_csv(csv_file)
    if df_logs is not None:
        print(df_logs)
        print(df_logs.dtypes)
except Exception as e:
    print("Erreur CSV :", e)


# c) API AbuseIPDB
try:
    df_api = extract_api(api_url, headers=headers)
    if df_api is not None:
        print("===== API AbuseIPDB =====")
        print(df_api.T)  # affichage transposé pour lisibilité
except Exception as e:
    print("Erreur API :", e)

# d) Base de données

connection_string = "sqlite:///data/raw/incidents.db"
query = "SELECT * FROM network_incidents WHERE status = 'login_attempt';"   
try:
    df_db = extract_db(connection_string, query)
    if df_db is not None:
        print(df_db)
        print(df_db.dtypes)
except Exception as e:
    print("Erreur DB :", e)




# -------------------------------
# 1️⃣ Extraction
# -------------------------------

# Depuis un CSV
df_csv = extract_csv(csv_file)

# Depuis un JSON
df_json = extract_json(json_file)

# Depuis une base SQLite
df_db = extract_db(connection_string, query)

# -------------------------------
# 2️⃣ Transformation
# -------------------------------

df_final = transform_data([df_csv, df_json, df_db])

# -------------------------------
# 3️⃣ Vérification
# -------------------------------

print("Colonnes après transformation :")
print(df_final.columns)
print("\nAperçu des 5 premières lignes :")
print(df_final.head())
print("\nInformations globales :")
print(df_final.info())

# -------------------------------
# 4️⃣ (Optionnel) Chargement
# -------------------------------
# Exemple : enregistrer en CSV
output_file = "data/processed/final_logs.csv"
df_final.to_csv(output_file, index=False)
load_csv(df_final, output_file)

import pandas as pd

# Chemin du fichier exporté
csv_file = "data/processed/final_logs.csv"

# Charger le CSV
df = pd.read_csv(csv_file)

# 1️⃣ Vérifier la taille du DataFrame
print(f"Nombre de lignes : {len(df)}")
print(f"Nombre de colonnes : {len(df.columns)}\n")

# 2️⃣ Vérifier les types de colonnes
print("Types de données par colonne :")
print(df.dtypes, "\n")

# 3️⃣ Vérifier les colonnes critiques
critical_cols = ["incident_id", "date", "status", "login_failed", "malware_detected"]
missing_cols = [col for col in critical_cols if col not in df.columns]
if missing_cols:
    print(f"⚠️ Colonnes critiques manquantes : {missing_cols}")
else:
    print("✅ Toutes les colonnes critiques sont présentes.\n")

# 4️⃣ Vérifier les valeurs nulles
print("Nombre de valeurs nulles par colonne :")
print(df.isnull().sum())
