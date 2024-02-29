import pandas as pd

class CSVReader:
    def __init__(self, delimiter=','):
        self.delimiter = delimiter

    def read_files(self, filepaths):
        dataframes = []
        for filepath in filepaths:
            try:
                df = pd.read_csv(filepath, delimiter=self.delimiter)
            except FileNotFoundError as e:
                raise FileNotFoundError(f"Fichier non trouvé: {e.filename}")
            dataframes.append(df)
        return pd.concat(dataframes)
