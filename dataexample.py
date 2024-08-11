import mysql.connector

# Establish a connection to the MySQL database
conn = mysql.connector.connect(
    host='localhost',       # e.g., 'localhost' or '127.0.0.1'
    user='dev2',   # e.g., 'root'
    password='Str0ngPssword',
    database='workmate'
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the SQL query to fetch 5 results from the table
query = "SELECT * FROM lab_data LIMIT 5"

# Execute the query
cursor.execute(query)

# Fetch the rows from the executed query
rows = cursor.fetchall()

# Get column names from the cursor description
columns = [desc[0] for desc in cursor.description]

# Close the cursor and connection
cursor.close()
conn.close()

# Format the results into a string
output = ''
for row in rows:
    for col_name, col_value in zip(columns, row):
        output += f'{col_name}: {col_value}\n'
    output += '\n'  # Separate each record with a newline

# Write the formatted string to a text file
with open('results.txt', 'w') as file:
    file.write(output)

print("Data fetching and writing to 'results.txt' is complete.")
