from tkinter import *
from tkinter import messagebox
import pymysql

def authenticate_user(username, password):
    mypass = "password_here"
    mydatabase = "database_name_here"

    con = pymysql.connect(host="localhost", user="root", password=mypass, database=mydatabase)
    cur = con.cursor()

    # Check if the username and password match a record in the users table
    query = "SELECT * FROM users WHERE username=%s AND password=%s"
    values = (username, password)

    try:
        cur.execute(query, values)
        user = cur.fetchone()

        if user:
            messagebox.showinfo("Success", "Login successful!")
            return True
        else:
            messagebox.showerror("Error", "Invalid username or password.")
            return False
    except Exception as e:
        messagebox.showerror("Error", f"Error during authentication: {str(e)}")
        return False
    finally:
        con.close()