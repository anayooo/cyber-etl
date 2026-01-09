# cyber-etl
ETL pipeline pour analyser des journaux de cybersécurité et enrichir des incidents avec des sources externes.

## Objectifs du projet
- Centraliser des données hétérogènes (CSV, JSON, API, base SQLite).
- Normaliser/enrichir les événements de sécurité via une étape de transformation.
- Produire un jeu de données final prêt pour l’analyse et la visualisation.

## Architecture technique (vue d’ensemble)
```
cyber-etl/
│
├── data/
│   ├── raw/              # données sources brutes
│   ├── processed/        # données transformées
│   └── logs/             # logs d’exécution du pipeline
│
├── etl/
│   ├── extract.py        # extraction (CSV, JSON, API, DB)
│   ├── transform.py      # nettoyage, normalisation, enrichissement
│   ├── load.py           # chargement/exports
│   ├── config.py         # variables d’environnement, clés API
│   └── utils.py          # fonctions utilitaires (logging, etc.)
│
├── dashboards/
│   └── grafana/          # fichiers de configuration Grafana/Kibana
│
├── notebooks/
│   └── exploration.ipynb # tests d'analyse et visualisation
│
├── create_tes_db.py      # génération d'une base SQLite d'exemple
├── main.py               # exécution complète du pipeline
├── .env.example          # exemple de configuration locale
├── requirements.txt      # dépendances Python
└── README.md
```

## Prérequis
- Python 3.9+ (recommandé).
- Accès réseau pour interroger l’API AbuseIPDB (si utilisée).

## Installation
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Données d’entrée attendues
- `data/raw/logs_auth.csv` : journaux d’authentification.
- `data/raw/malware.json` : événements liés aux malwares.
- `data/raw/incidents.db` : base SQLite d’incidents réseau.

Pour générer une base SQLite d’exemple :
```bash
python create_tes_db.py
```

## Exécution du pipeline
Le script `main.py` orchestre l’extraction, la transformation et l’export final :
```bash
python main.py
```

Le pipeline :
1. **Extrait** les données depuis CSV, JSON, API et SQLite.
2. **Transforme** et normalise les champs pour un format unifié.
3. **Exporte** le résultat dans `data/processed/final_logs.csv`.

## Configuration (API AbuseIPDB)
Le script `main.py` utilise une clé d’API définie dans le code. Pour un usage propre :
1. Créez un fichier `.env`.
2. Ajoutez-y votre clé, par exemple :
   ```env
   ABUSEIPDB_API_KEY=your_api_key_here
   ```
3. Vous pouvez partir du modèle `.env.example` fourni à la racine.
4. Utilisez cette variable dans `etl/config.py` ou `main.py` (bonne pratique).

## Exemple de flux de travail
```bash
python create_tes_db.py
python main.py
```

## Résultat attendu
- Un fichier consolidé `data/processed/final_logs.csv` contenant des colonnes issues de chaque source.
- Des impressions console qui listent la structure des données et des vérifications basiques.

## Technologies utilisées
- Python (pandas, requests, sqlite3)
- SQLite
- Outils de visualisation (Grafana/Kibana) via le dossier `dashboards/`
