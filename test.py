import pandas as pd

def extract_first_3000_rows(excel_file, output_csv_file):
    # Read the Excel file
    df = pd.read_csv(excel_file)

    # Extract the first 3000 rows
    df_first_3000 = df.iloc[:3000]

    # Write to a new CSV file
    df_first_3000.to_csv(output_csv_file, index=False)

    print(f'{output_csv_file} created with the first 3000 rows')

# Usage
excel_file = 'patient_notes.csv'
output_csv_file = 'any.csv'
extract_first_3000_rows(excel_file, output_csv_file)
