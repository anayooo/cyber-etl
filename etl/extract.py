
import pandas as pd                             #permet de manipuler et analyser des données tabulaires (Dataframe)
import requests                                 #permet de faire des requêtes HTTP, utiles pour récupérer des données depuis des APIs
from sqlalchemy import create_engine            #sert à créer une connexion à une base de données (SQL) de façon flexible

def extract_csv(path):
    return pd.read_csv(path)

def extract_api(url, headers=None):
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return pd.DataFrame(response.json())

def extract_db(connection_string, query):
    engine = create_engine(connection_string)
    return pd.read_sql(query, engine)

