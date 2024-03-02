import pandas as pd

class CSVReader:
    def read(self, file_path):
        return pd.read_csv(file_path)

