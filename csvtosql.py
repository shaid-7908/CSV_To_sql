import pandas as pd
import mysql.connector
from mysql.connector import Error

# Read the CSV file
csv_file_path = '/mnt/data/cutomer.csv'
df = pd.read_csv(csv_file_path)

# Database connection details
host = 'your_mysql_host'
database = 'your_database_name'
user = 'your_username'
password = 'your_password'

# Create a connection to the database
try:
    connection = mysql.connector.connect(
        host=host,
        database=database,
        user=user,
        password=password
    )

    if connection.is_connected():
        cursor = connection.cursor()

        # Assuming the table name is 'customers' and the columns match the DataFrame columns
        for i, row in df.iterrows():
            sql_query = """INSERT INTO customers (column1, column2, column3, ...) 
                           VALUES (%s, %s, %s, ...)"""
            cursor.execute(sql_query, tuple(row))

        connection.commit()
        print("Data inserted successfully")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
