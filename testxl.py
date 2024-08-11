import pandas as pd

def extract_random_100_rows(excel_file, output_csv_file):
    # Read the Excel file
    df = pd.read_excel(excel_file)

    # Ensure we have at least 100 rows to sample from
    num_rows = min(100, len(df))

    # Randomly select 100 rows
    df_random_100 = df.sample(n=num_rows, random_state=1)

    # Write to a new CSV file
    df_random_100.to_csv(output_csv_file, index=False)

    print(f'{output_csv_file} created with {num_rows} random rows')

# Usage
excel_file = 'BCMserv324.xlsx'
output_csv_file = 'random_100_rows.csv'
extract_random_100_rows(excel_file, output_csv_file)
