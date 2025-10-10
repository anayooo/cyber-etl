# cyber-etl
ETL pipeline for cybersecurity log analysis and threat intelligence.

Architecture technique golbale

cyber-etl/
│
├── data/
│   ├── raw/              # données sources brutes
│   ├── processed/        # données transformées
│   └── logs/             # logs d’exécution du pipeline
│
├── etl/
│   ├── extract.py        # extraction (CSV, API, DB)
│   ├── transform.py      # nettoyage, normalisation, enrichissement
│   ├── load.py           # insertion en base
│   ├── config.py         # variables d’environnement, clés API
│   └── utils.py          # fonctions utilitaires (logging, etc.)
│
├── dashboards/
│   └── grafana/          # fichiers de configuration Grafana/Kibana
│
├── notebooks/
│   └── exploration.ipynb # tests d'analyse, visualisation
│
├── docker-compose.yml    # conteneurisation
├── requirements.txt      # dépendances Python
└── README.md

Objectifs du projet


Technologies utilisées


Instructions pour installer et exécuter


Sources de données et exemples
