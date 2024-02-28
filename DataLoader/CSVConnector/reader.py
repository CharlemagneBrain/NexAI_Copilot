import csv
import pandas as pd

class CSVReader:
    def read_files(self, filepaths):
        data = []
        for filepath in filepaths:
            try:
                df = pd.read_csv(filepath)
            except FileNotFoundError:
                raise FileNotFoundError(f"Fichier non trouvé: {filepath}")
            data.append(df)
        return pd.concat(data)