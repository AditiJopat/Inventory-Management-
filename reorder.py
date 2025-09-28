#!C:\Users\USER\AppData\Local\Microsoft\WindowsApps\python.exe
import cgi
import cgitb
import sqlite3

# Enable CGI error reporting for easier debugging
cgitb.enable()

# Establish connection to SQLite database
db_name = "project.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Define the HTML and CSS for the web page
header_html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inventory Management System - Item Reorder Levels</title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
            background-color: #f8f8f8;
            color: #333;
            margin: 0;
        }

        header, footer {
            background-color: #cc0000;
            color: white;
            padding: 10px 20px;
            text-align: center;
        }

        .container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            background-color: #fff;
            margin-top: 20px;
        }

        h1 {
            text-align: center;
            color: #cc0000;
            margin-bottom: 20px;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }

        table, th, td {
            border: 1px solid #ccc;
        }

        th, td {
            padding: 10px;
            text-align: left;
        }

        th {
            background-color: #cc0000;
            color: white;
        }

        .button-container {
            text-align: center;
            margin-top: 20px;
        }

        .button {
            background-color: #cc0000;
            color: white;
            padding: 10px 20px;
            font-size: 16px;
            border: none;
            cursor: pointer;
            border-radius: 5px;
        }
    </style>
</head>
<body>
    <header>
        <h1>Inventory Management System - Item Reorder Levels</h1>
    </header>
    <div class="container">
"""

footer_html = """
    </div>
    <footer>
        <p>&copy; 2024 Inventory Management System. All rights reserved.</p>
    </footer>
</body>
</html>
"""

# Print the initial content-type and header HTML
print("Content-type: text/html\n")
print(header_html)

# Fetch and display items with their reorder levels from the database
def display_item_table():
    cursor.execute("SELECT itemid, reorderlvl, itemname FROM itemtable")
    rows = cursor.fetchall()
    if rows:
        print("<h2>Table: REORDER LEVEL</h2>")
        print("<table>")
        print("<tr><th>Item ID</th><th>Item Name</th><th>Reorder Level</th></tr>")
        for row in rows:
            print(f"<tr><td>{row[0]}</td><td>{row[2]}</td><td>{row[1]}</td></tr>")
        print("</table>")
    else:
        print("<p>No items found.</p>")

# Display item table initially
display_item_table()

# HTML form for checking items below reorder level
print("""
    <div class="button-container">
        <form method="post" action="itembelowreorder.py">
            <button type="submit" class="button" name="check_reorder_button">Check Items Below Reorder Level</button>
        </form>
    </div>
""")

# Print the footer HTML
print(footer_html)

# Close the database connection
conn.close()
