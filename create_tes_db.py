import sqlite3
import random
from datetime import datetime, timedelta

# Connexion à la base (créée automatiquement si elle n'existe pas)
conn = sqlite3.connect("data/raw/incidents.db")
cursor = conn.cursor()

# Suppression de la table si elle existe déjà
cursor.execute("DROP TABLE IF EXISTS network_incidents;")

# Création de la table
cursor.execute("""
CREATE TABLE network_incidents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    timestamp TEXT,
    source_ip TEXT,
    destination_ip TEXT,
    event_type TEXT,
    status TEXT,
    user_id TEXT,
    login_failed INTEGER,
    malware_detected INTEGER,
    response_time REAL,
    downtime_duration REAL
);
""")

# Génération de données aléatoires
event_types = ["login_attempt", "data_access", "file_upload", "network_scan"]
statuses = ["success", "failure", "pending"]
base_time = datetime.now()

rows = []
for _ in range(200):
    row = (
        (base_time - timedelta(minutes=random.randint(0, 50000))).isoformat(),
        f"192.168.1.{random.randint(1, 255)}",
        f"10.0.0.{random.randint(1, 255)}",
        random.choice(event_types),
        random.choice(statuses),
        f"user_{random.randint(1, 20)}",
        random.randint(0, 1),
        random.randint(0, 1),
        round(random.uniform(0.5, 20.0), 2),
        round(random.uniform(0.0, 10.0), 2),
    )
    rows.append(row)

# Insertion dans la base
cursor.executemany("""
INSERT INTO network_incidents (
    timestamp, source_ip, destination_ip, event_type, status,
    user_id, login_failed, malware_detected, response_time, downtime_duration
)
VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
""", rows)

conn.commit()
conn.close()

print("✅ Base SQLite créée avec succès : data/raw/incidents.db")
print("✅ Table : network_incidents (200 lignes générées)")
