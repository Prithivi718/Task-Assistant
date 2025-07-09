# import csv
# import sqlite3

# # Connect to the jarvis.db database (it will create the file if it doesn't exist)
# conn = sqlite3.connect('jarvis.db')
# cursor = conn.cursor()

# # query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
# # cursor.execute(query)

# # Insertion into sys_command
# # query = r"INSERT INTO sys_command VALUES(null, 'chrome', 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe')"
# # cursor.execute(query)
# # conn.commit()

# # query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
# # cursor.execute(query)

# # Insertion into web_command
# # query = r"INSERT INTO web_command VALUES(null, 'whatsapp', 'https://web.whatsapp.com/')"
# # cursor.execute(query)
# # conn.commit()

# #Creating contacts table for JARVIS WhatsApp functionality
# # Create contacts table if not exists
# cursor.execute('''
#     CREATE TABLE IF NOT EXISTS contacts (
#         id INTEGER PRIMARY KEY,
#         name VARCHAR(200),
#         mobile_no VARCHAR(255),
#         email VARCHAR(255) NULL
#     )
# ''')

# # Clean and insert contacts from CSV
# desired_columns_indices = [0, 18]  # Adjust based on your file

# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         try:
#             selected_data = [row[i] for i in desired_columns_indices]
#             cursor.execute('''INSERT INTO contacts (id, name, mobile_no) VALUES (null, ?, ?)''', tuple(selected_data))
#         except Exception as e:
#             print(f"Error inserting row: {e}")
# # query = 'sukesh'
# # query = query.strip().lower()

# # cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# # results = cursor.fetchall()

# # Commit changes and close connection
# conn.commit()

