import pandas as pd
from ..utils import check_columns, check_unique_index
from CSVConnector.reader import CSVReader

class TSVReader(CSVReader):
    def __init__(self):
        super().__init__(delimiter='\t')
