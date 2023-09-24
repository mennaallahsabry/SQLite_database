# Open the database connection
import datacreate
import sqlite3
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()
# Open the image file and read binary data using a raw string literal
with open(r"D:\fastapi-starter-template\dog.jpg", "rb") as image_file:
    image_binary_data = image_file.read()

# Insert a sample record
cursor.execute("INSERT INTO my_table (name, phone_number, image, serial_number) VALUES (?, ?, ?, ?)",("Jooe", "555-323-4577", image_binary_data, "1775"))

# Commit the changes and close the connection
try:
    # Insert data or perform other database operations here
    conn.commit()
except sqlite3.Error as e:
    print("SQLite error:", e)
finally:
    conn.close()

