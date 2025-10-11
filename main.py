# main.py
import os
from dotenv import load_dotenv
import pandas as pd
from etl.extract import extract_csv, extract_json, extract_api, extract_db

# -------------------------------------------------
# 1️⃣ Charger les variables d'environnement
# -------------------------------------------------
load_dotenv()
api_key = "2feaaf26759da77632157d11acb8edb345ebd759094abfdad3679bdee1d26a484866bf975dbe7820"

# -------------------------------------------------
# 2️⃣ Définir les fichiers et paramètres
# -------------------------------------------------
# Fichiers locaux
csv_file = r"C:\Users\HP\Desktop\Python\Cyber ETL\cyber-etl\data\raw\Financial Data Set.csv"
json_file = r"C:\Users\HP\Desktop\Python\Cyber ETL\cyber-etl\data\raw\user_activity_data.json"

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

connection_string = "sqlite:///data/raw/cyber_logs.db"
query = "SELECT * FROM logs WHERE event_type = 'login_attempt';"
try:
    df_db = extract_db(connection_string, query)
    if df_db is not None:
        print(df_db)
        print(df_db.dtypes)
except Exception as e:
    print("Erreur DB :", e)