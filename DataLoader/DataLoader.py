import argparse
from CSVConnector.reader import CSVReader
from TSVConnector.reader import TSVReader

class DataLoader:
    def __init__(self):
        self.parsers = {'csv': CSVReader(), 'tsv': TSVReader()}

    def load_data(self, file_type, filepaths):
        reader = self.parsers.get(file_type.lower())
        if reader is None:
            raise ValueError("Type de fichier non pris en charge")
        return reader.read_files(filepaths)

def main(args):
    loader = DataLoader()
    data = loader.load_data(args.type, args.files)
    print(data.head())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chargeur de données")
    parser.add_argument("type", help="Type de fichier (CSV ou TSV)")
    parser.add_argument("files", nargs="+", help="Chemins des fichiers")
    args = parser.parse_args()
    
    main(args)
