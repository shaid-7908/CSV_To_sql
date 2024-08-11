import pymysql
import pandas as pd

# Database connection parameters
db_user = 'dev2'
db_password = 'Str0ngPssword'
db_host = 'localhost'
db_port = 3306
db_name = 'workmate'

# Output file path
output_file = 'tables_info.txt'

# Connect to the MySQL database
connection = pymysql.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name,
    port=db_port
)

try:
    # Query to get all tables in the database
    tables_query = "SHOW TABLES"
    tables_df = pd.read_sql(tables_query, connection)
    
    table_info_list = []

    for table in tables_df.values.flatten():
        # Query to get information about each table
        table_info_query = f"SHOW COLUMNS FROM {table}"
        table_info_df = pd.read_sql(table_info_query, connection)
        
        # Add the table name to the DataFrame
        table_info_df['Table'] = table
        table_info_list.append(table_info_df)

    # Concatenate all the table information DataFrames
    all_tables_info_df = pd.concat(table_info_list)
    
    # Reorder columns to have 'Table' as the first column
    all_tables_info_df = all_tables_info_df[['Table'] + [col for col in all_tables_info_df.columns if col != 'Table']]
    
    # Write the DataFrame to a text file
    with open(output_file, 'w') as f:
        for table in tables_df.values.flatten():
            f.write(f"Table: {table}\n")
            table_info_query = f"SHOW COLUMNS FROM {table}"
            table_info_df = pd.read_sql(table_info_query, connection)
            f.write(table_info_df.to_string(index=False))
            f.write("\n\n")
    
    print(f"Table information has been written to {output_file}")
    
finally:
    # Close the database connection
    connection.close()
