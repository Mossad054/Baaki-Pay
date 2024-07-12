import sqlite3

conn = sqlite3.connect('database/mydatabase.db')
cursor = conn.cursor()

# Create the merchants table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS merchants (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Table 'merchants' created successfully.")
