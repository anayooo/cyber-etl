import pandas as pd

# -------------------------------
# Harmonisation des colonnes
# -------------------------------
def harmonize_columns(df):
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df

# -------------------------------
# Conversion des dates
# -------------------------------
def convert_dates(df):
    for col in df.columns:
        if "date" in col or "time" in col or "timestamp" in col:
            df[col] = pd.to_datetime(df[col], errors="coerce")
    return df

# -------------------------------
# Gestion des valeurs manquantes
# -------------------------------
def handle_missing_values(df):
    df.fillna("", inplace=True)
    return df

# -------------------------------
# Ajout d'indicateurs cybersécurité
# -------------------------------
def add_indicators(df):
    # Exemple : login_failed
    if "status" in df.columns:
        df["login_failed"] = df["status"].apply(
            lambda x: 1 if isinstance(x, str) and x.lower() == "failed" else 0
        )
    # Tu peux ajouter d'autres indicateurs ici
    # Exemple : malware_detected
    if "event_type" in df.columns:
        df["malware_detected"] = df["event_type"].apply(
            lambda x: 1 if isinstance(x, str) and "malware" in x.lower() else 0
        )
    return df

# -------------------------------
# Fonction principale de transformation
# -------------------------------
def transform_data(dataframes):
    # 1️⃣ Fusionner les DataFrames
    df = pd.concat(dataframes, ignore_index=True)

    # 2️⃣ Harmoniser les colonnes
    df = harmonize_columns(df)

    # 3️⃣ Convertir les colonnes de date
    df = convert_dates(df)

    # 4️⃣ Ajouter des indicateurs cybersécurité
    df = add_indicators(df)

    # 5️⃣ Gérer les valeurs manquantes
    df = handle_missing_values(df)

    return df
