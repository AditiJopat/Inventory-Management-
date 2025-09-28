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

# Function to calculate quantity available
def calculate_quantity_available(item_id):
    cursor.execute("SELECT SUM(issuequantity) FROM ivtable WHERE itemid=?", (item_id,))
    total_issue_quantity = cursor.fetchone()[0] or 0  # Fetch the sum of issue quantity
    cursor.execute("SELECT SUM(quantitybought) FROM rvtable WHERE itemid=?", (item_id,))
    quantity_bought = cursor.fetchone()[0] or 0  # Fetch the sum of quantity bought
    quantity_available = quantity_bought - total_issue_quantity
    return quantity_available

# Generate HTML response
print("Content-type: text/html\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Items Below Reorder Level</title>
    <style>
        body {
            font-family: 'Poppins', sans-serif;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin-top: 20px;
        }
        table, th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        th {
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: left;
            background-color: #4CAF50;
            color: white;
        }
        td {
            text-align: center;
        }
    </style>
</head>
<body>
    <h1>Items Below Reorder Level</h1>
    <table>
        <tr>
            <th>Item ID</th>
            <th>Item Name</th>
            <th>Reorder Level</th>
            <th>Quantity Available</th>
        </tr>
""")

# Fetch items with reorder levels
cursor.execute("SELECT itemid, itemname, reorderlvl FROM itemtable")
items = cursor.fetchall()

# Check and display items below reorder level
items_below_reorder = False
for item in items:
    item_id, item_name, reorder_level = item
    quantity_available = calculate_quantity_available(item_id)
    if quantity_available < reorder_level:
        items_below_reorder = True
        print(f"<tr><td>{item_id}</td><td>{item_name}</td><td>{reorder_level}</td><td>{quantity_available}</td></tr>")

if not items_below_reorder:
    print("<tr><td colspan='4' style='text-align:center;'>No items below reorder level.</td></tr>")

print("""
    </table>
</body>
</html>
""")

cursor.close()
conn.close()