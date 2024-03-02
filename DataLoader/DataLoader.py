import argparse
from CSVConnector.reader import CSVReader
from TSVConnector.reader import TSVReader
from pandas import DataFrame

def load_data(file_paths):
    dataframes = []
    for file_path in file_paths:
        if file_path.endswith('.csv'):
            reader = CSVReader()
            df = reader.read(file_path)
        elif file_path.endswith('.tsv'):
            reader = TSVReader()
            df = reader.read(file_path)
        else:
            raise ValueError("Unsupported file format")
        dataframes.append(df)
    return dataframes

def integrate_dataframes(dataframes):
    # Assuming all dataframes have the same columns
    return DataFrame(pd.concat(dataframes, ignore_index=True))

def main():
    parser = argparse.ArgumentParser(description='Load and integrate CSV or TSV files')
    parser.add_argument('--type', choices=['csv', 'tsv'], help='Type of files to load')
    parser.add_argument('files', nargs='+', help='List of file paths to load')
    args = parser.parse_args()

    if args.type == 'csv':
        file_paths = args.files
    elif args.type == 'tsv':
        file_paths = args.files
    else:
        raise ValueError("Unsupported file format")

    dataframes = load_data(file_paths)
    integrated_df = integrate_dataframes(dataframes)
    print(integrated_df)

if __name__ == "__main__":
    main()
