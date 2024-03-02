import pandas as pd

class TSVReader:
    def read(self, file_path):
        return pd.read_csv(file_path, sep='\t')
