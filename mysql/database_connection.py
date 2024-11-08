import mysql.connector
from mysql.connector import Error


try:
    connection = mysql.connector.connect(
        host="localhost",        
        user="root",             
        password="Yogesh@15"
    )

    if connection.is_connected():
        print("Connected to MySQL server")

        
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS sports_db")
        print("Database 'sports_db' is created")

        
        cursor.execute("USE sports_db")

        
        create_table_query = """
        CREATE TABLE IF NOT EXISTS sports_events (
            event_id INT AUTO_INCREMENT PRIMARY KEY,
            event_name VARCHAR(255) NOT NULL,
            event_date DATE NOT NULL,
            sport_type VARCHAR(100) NOT NULL,
            team1 VARCHAR(100),
            team2 VARCHAR(100),
            location VARCHAR(255),
            winner VARCHAR(100)
        )
        """
        cursor.execute(create_table_query)
        print("Table 'sports_events' created or already exists")

        
        insert_data_query = """
        INSERT INTO sports_events (event_name, event_date, sport_type, team1, team2, location, winner)
        VALUES
        ('Basketball Championship', '2024-11-20', 'Basketball', 'Team A', 'Team B', 'Stadium A', 'Team A'),
        ('Football Tournament', '2024-11-25', 'Football', 'Team C', 'Team D', 'Stadium B', 'Team D'),
        ('Swimming Competition', '2024-12-05', 'Swimming', NULL, NULL, 'Aquatic Center', 'N/A')
        """
        cursor.execute(insert_data_query)
        connection.commit()
        print("Sample data inserted into 'sports_events' table")

except Error as e:
    print("Error connecting to MySQL", e)

finally:
    
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection closed")
