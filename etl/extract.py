
import pandas as pd                             #permet de manipuler et analyser des données tabulaires (Dataframe)
import requests
import json                                 #permet de faire des requêtes HTTP, utiles pour récupérer des données depuis des APIs
from sqlalchemy import create_engine            #sert à créer une connexion à une base de données (SQL) de façon flexible

#Extraction csv
def extract_csv(path):
    return pd.read_csv(path)


#Extraction Json local
def extract_json(path):
    with open(path, 'r') as f:
        data = json.load(f)
    return pd.json_normalize(data)


def extract_api(url, headers=None):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return pd.DataFrame(response.json())


def extract_db(connection_string, query):
    """
    connection_string : str, ex: 'postgresql+psycopg2://user:password@host:port/dbname'
    query : str, requête SQL pour extraire les données
    """
    engine = create_engine(connection_string)
    with engine.connect() as conn:
        df = pd.read_sql(query, conn)
    return df

