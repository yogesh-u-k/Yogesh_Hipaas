import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read the credentials from environment variables
db_host = os.getenv("DB_HOST")
db_user = os.getenv("DB_USER")
db_password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

with open("D:\Yogesh_Hipass\\EDI\\edi.txt") as txtfile:
    data = txtfile.read()

# Connect to the database using the environment variables
db = mysql.connector.connect(
    host=db_host,
    user=db_user,
    password=db_password,
    database=db_name
)

cursor = db.cursor()

# Process and insert data as in the previous example
res = data.split("~")
result = []
result2 = []

n = len(res)

for i in range(n):
    value = res[i].split("*")
    result.append(value[0])

for j in range(n - 1):
    value1 = res[j].split("*")
    result2.append(value1[1])

# Prepare the insert query with placeholders
insert_query = "INSERT INTO edi_data (segment, firstvalue) VALUES (%s, %s)"
data_to_insert = list(zip(result, result2))

for row in data_to_insert:
    cursor.execute(insert_query, row)

db.commit()
print("Data inserted successfully")

# Close the connection
db.close()
