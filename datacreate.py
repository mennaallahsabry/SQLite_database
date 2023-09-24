import sqlite3

# Create a connection to the SQLite database (or create a new one if it doesn't exist)
conn = sqlite3.connect('my_database.db')

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store the information
cursor.execute('''
    CREATE TABLE IF NOT EXISTS my_table (
        id INTEGER PRIMARY KEY,
        name TEXT,
        phone_number TEXT,
        image BLOB,  -- BLOB type for storing binary data like images
        serial_number TEXT
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
