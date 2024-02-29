import pandas as pd

def check_columns(dataframes):
   
    cols = [set(df.columns) for df in dataframes]
    if len(set(cols)) != 1:
        raise ValueError("Les colonnes des fichiers ne correspondent pas")
    return cols[0]

def check_unique_index(dataframes):
    
    indices = [df.index.is_unique for df in dataframes]
    if not all(indices):
        raise ValueError("Les index des fichiers ne sont pas uniques")
