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

def determine_integration_operation(dataframes):
   
    all_columns = [set(df.columns) for df in dataframes]
    common_columns = set.intersection(*all_columns)

    if len(common_columns) == len(all_columns[0]):
        return 'concatenation'
    elif common_columns:
        return 'jointure'
    else:
        return 'union'

