import pandas as pd
from sqlalchemy import create_engine

# -------------------------------
# Export CSV
# -------------------------------
def load_csv(df, output_path):
    """
    Charge le DataFrame dans un fichier CSV.
    
    df : pandas.DataFrame
    output_path : str, chemin du fichier CSV
    """
    df.to_csv(output_path, index=False)
    print(f"✅ DataFrame final exporté en CSV : {output_path}")


# -------------------------------
# Export Parquet (optionnel)
# -------------------------------
def load_parquet(df, output_path):
    df.to_parquet(output_path, index=False)
    print(f"✅ DataFrame final exporté en Parquet : {output_path}")


# -------------------------------
# Export dans une base SQL (optionnel)
# -------------------------------
def load_db(df, connection_string, table_name, if_exists="replace"):
    """
    Charge le DataFrame dans une base SQL.
    
    df : pandas.DataFrame
    connection_string : str, ex: 'sqlite:///data/processed/cyber_logs.db'
    table_name : str, nom de la table SQL
    if_exists : str, "replace" ou "append"
    """
    engine = create_engine(connection_string)
    df.to_sql(table_name, con=engine, if_exists=if_exists, index=False)
    print(f"✅ DataFrame final chargé dans la table '{table_name}' de la base")
