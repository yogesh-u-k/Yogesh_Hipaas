import pandas as pd
from mysql.connector import Error
import mysql.connector
import numpy as np

try:
    # Load Excel file
    excel_file = "D:\\Yogesh_Hipass\\Excel_database\\StudentPerformanceFactors.csv"
    df = pd.read_csv(excel_file)

    # Check if DataFrame is empty
    if df.empty:
        print("The DataFrame is empty!")
    else:
        print(f"The DataFrame has {len(df)} rows.")
    
    # Replace NaN values with None to handle SQL NULL values
    df = df.replace({np.nan: None})

    # Print DataFrame columns and data types for debugging
    print("Columns in DataFrame:", df.columns)
    print("Data types in DataFrame:", df.dtypes)

    # Connect to MySQL
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Yogesh@15",
        database="student_performance"
    )

    if db.is_connected():
        print("Connected to MySQL server")

        cursor = db.cursor()
        # Define table name
        table_name = "student_pr"

        # Dynamically create table based on DataFrame columns if it doesn't exist
        def create_table_if_not_exists(cursor, table_name, df):
            # Map DataFrame dtypes to MySQL data types
            dtype_mapping = {
                'object': 'VARCHAR(255)',
                'int64': 'INT',
                'float64': 'FLOAT',
                'datetime64[ns]': 'DATETIME'
            }

            # Generate column definitions
            columns = []
            for column_name, dtype in df.dtypes.items():
                sql_dtype = dtype_mapping.get(str(dtype), 'VARCHAR(255)')
                columns.append(f"{column_name} {sql_dtype}")

            # Join column definitions with commas
            columns_sql = ", ".join(columns)

            # Create table SQL
            create_table_query = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns_sql})"
            cursor.execute(create_table_query)

        # Call the function to create the table
        create_table_if_not_exists(cursor, table_name, df)

        # Prepare the dynamic insert query
        columns = ", ".join(df.columns)
        placeholders = ", ".join(["%s"] * len(df.columns))
        insert_query = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
        
        print("Insert Query:", insert_query)

        # Iterate over DataFrame rows as tuples
        for row in df.itertuples(index=False, name=None):
            try:
                cursor.execute(insert_query, row)
            except Error as e:
                print(f"Error executing query: {insert_query} with row: {row}")
                print("MySQL error:", e)

        # Commit transaction and close connection
        db.commit()
        print("Data imported successfully.")

except Error as e:
    print("Error connecting to MySQL", e)

finally:
    # Close the cursor and database connection
    if 'cursor' in locals():
        cursor.close()
    if 'db' in locals() and db.is_connected():
        db.close()
        print("MySQL connection closed.")
