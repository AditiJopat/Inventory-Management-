#!C:\Users\user\AppData\Local\Programs\Python\Python37\python.exe
import os
import cgi
import cgitb
import sqlite3

cgitb.enable()
print("Content-type: text/html\n\n")
print("<html><body style='text-align:center;'>")
print("<h1 style='color: #800000;'>LOGIN PAGE</h1>")
form = cgi.FieldStorage()
db_name = "venkat21.db"
name = ""
pwd = ""

if os.environ['REQUEST_METHOD'].upper() == 'POST':
    if form.getvalue("username"):
        name = form.getvalue("username")
    if form.getvalue("password"):
        pwd = form.getvalue("password")
    
    def connect_to_db(db_name):
        try:
            con = sqlite3.connect(db_name)
            return con
        except sqlite3.Error as error:
            print("<p>Error while connecting to SQLite: " + str(error) + "</p>")
            return None
    
    con = connect_to_db(db_name)

    if con:
        try:
            cur = con.cursor()
            sql_select = "SELECT designation FROM signup WHERE username = ? AND password = ?"
            cur.execute(sql_select, (name, pwd))
            rec = cur.fetchone()
            if rec:
                designation = rec[0]
                if designation == 'hod':
                    print('<meta http-equiv="refresh" content="0;url=hod.html" />')
                elif designation == 'admin':
                    print('<meta http-equiv="refresh" content="0;url=inventory.html" />')
                elif designation == 'storekeeper':
                    print('<meta http-equiv="refresh" content="0;url=store.html" />')    
                elif designation == 'director':
                    print('<meta http-equiv="refresh" content="0;url=director.html" />')
                elif designation == 'inventory':
                    print('<meta http-equiv="refresh" content="0;url=indeventoryman.html" />')
                
                else:
                    print("<script>alert('Designation not recognized.'); window.location.href = 'login_form.html';</script>")
            else:
                print("<script>alert('Login failed. Please try again.'); window.location.href = 'login_form.html';</script>")
        except sqlite3.Error as error:
            print("<p>Error while executing SQL query: " + str(error) + "</p>")
        finally:
            con.close()
    else:
        print("<p>Failed to connect to the database</p>")

print("</body></html>")
