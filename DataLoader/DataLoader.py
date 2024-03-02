import argparse
import pandas as pd
from CSVConnector.reader import CSVReader
from TSVConnector.reader import TSVReader

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
    
    same_structure = all(dataframes[0].columns.equals(df.columns) for df in dataframes)
    if same_structure:
       
        integrated_df = pd.concat(dataframes, ignore_index=True)
    else:

        common_columns = set(dataframes[0].columns)
        for df in dataframes[1:]:
            common_columns &= set(df.columns)
        if common_columns:
            
            integrated_df = pd.concat([df.set_index(list(common_columns)) for df in dataframes], axis=1).reset_index()
        else:
            
            integrated_df = pd.concat(dataframes, ignore_index=True)
    return integrated_df


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
    print(integrated_df.head())

if __name__ == "__main__":
    main()
