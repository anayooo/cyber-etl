import json, random
from datetime import datetime, timedelta


malware_types = ["ransomware", "trojan", "worm", "adware"]
data_json = []
for i in range(30):
    data_json.append({
        "device_id": f"device_{i+1}",
        "timestamp": (datetime.now() - timedelta(hours=random.randint(0,48))).isoformat(),
        "malware_type": random.choice(malware_types),
        "detected": random.choice([0,1])
    })

with open("data/raw/malware.json", "w") as f:
    json.dump(data_json, f, indent=4)
print("✅ JSON généré : data/raw/malware.json")
