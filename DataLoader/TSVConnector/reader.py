import csv
import pandas as pd

class TSVReader:
    def read_files(self, filepaths):
        data = []
        for filepath in filepaths:
            try:
                df = pd.read_csv(filepath, delimiter="\t")
            except FileNotFoundError:
                raise FileNotFoundError(f"Fichier non trouvé: {filepath}")
            data.append(df)
        return pd.concat(data)