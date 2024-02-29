import pandas as pd
from CSVConnector import CSVReader

class TSVReader(CSVReader):
    def __init__(self):
        super().__init__(delimiter='\t')
