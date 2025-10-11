import pandas as pd
import random
from datetime import datetime, timedelta

# Génération de 50 logs utilisateurs
users = [f"user{i}" for i in range(1, 11)]
statuses = ["success", "failed"]

data_csv = []
for i in range(50):
    data_csv.append({
        "userid": random.choice(users),
        "timestamp": (datetime.now() - timedelta(days=random.randint(0,10))).strftime("%Y-%m-%d %H:%M:%S"),
        "status": random.choice(statuses),
        "source_ip": f"192.168.1.{random.randint(1,50)}"
    })

df_csv = pd.DataFrame(data_csv)
df_csv.to_csv("data/raw/logs_auth.csv", index=False)
print("✅ CSV généré : data/raw/logs_auth.csv")
