import sqlite3
import pandas as pd

# Chemin du fichier SQLite
db_path = "data/raw/cyber_logs.db"

# Connexion à la DB (si le fichier n'existe pas, il sera créé)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Création de la table logs
cursor.execute("""
CREATE TABLE IF NOT EXISTS logs (
    id INTEGER PRIMARY KEY,
    timestamp TEXT,
    source_ip TEXT,
    destination_ip TEXT,
    event_type TEXT,
    status TEXT
)
""")

# Exemple de données
logs = [
    ("2025-10-11T10:15:00", "192.168.1.10", "10.0.0.5", "login_attempt", "failed"),
    ("2025-10-11T10:17:00", "192.168.1.12", "10.0.0.5", "login_attempt", "success"),
    ("2025-10-11T10:20:00", "192.168.1.15", "10.0.0.7", "file_access", "denied"),
    ("2025-10-11T10:25:00", "192.168.1.20", "10.0.0.9", "malware_detected", "quarantined")
]

# Insertion des données
cursor.executemany("""
INSERT INTO logs (timestamp, source_ip, destination_ip, event_type, status)
VALUES (?, ?, ?, ?, ?)
""", logs)

# Valider et fermer
conn.commit()
conn.close()

print(f"Base SQLite créée et peuplée ici : {db_path}")
