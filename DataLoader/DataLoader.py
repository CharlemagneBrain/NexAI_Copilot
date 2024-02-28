import argparse
import csv
from CSVConnector.reader import CSVReader
from TSVConnector.reader import TSVReader

def main(args):
    file_type = args.type.lower()

    if file_type not in ("csv", "tsv"):
        raise ValueError("Type de fichier non pris en charge")

    filepaths = args.files

    if file_type == "csv":
        reader = CSVReader()
    elif file_type == "tsv":
        reader = TSVReader()
    data = reader.read_files(filepaths)

    print(data.head())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Chargeur de données")
    parser.add_argument("type", help="Type de fichier (CSV ou TSV)")
    parser.add_argument("files", nargs="+", help="Chemins des fichiers")
    args = parser.parse_args()
    
    main(args)