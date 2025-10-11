from sqlalchemy import create_engine
import random
import pandas as pd
from datetime import datetime, timedelta


engine = create_engine("sqlite:///data/raw/incidents.db")
incident_types = ["DDoS", "Phishing", "Data Leak", "Unauthorized Access"]

data_db = []
for i in range(40):
    data_db.append({
        "incident_id": f"INC{i+1:03d}",
        "date": (datetime.now() - timedelta(days=random.randint(0,20))).strftime("%Y-%m-%d"),
        "incident_type": random.choice(incident_types),
        "severity": random.choice(["Low", "Medium", "High"]),
        "resolved": random.choice([0,1])
    })

df_db = pd.DataFrame(data_db)
df_db.to_sql("network_incidents", con=engine, if_exists="replace", index=False)
print("✅ Base SQL générée : data/raw/incidents.db (table network_incidents)")
