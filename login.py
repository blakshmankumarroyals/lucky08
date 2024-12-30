import streamlit as st
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create users table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        password TEXT NOT NULL
    )
''')
conn.commit()

# Set the title of the app
st.title("Login")

# Create a form for login
with st.form("login_form"):
    username = st.text_input("Username", value="", max_chars=50)
    password = st.text_input("Password", type="password", value="", max_chars=50)
    
    # Add a submit button
    submit_button = st.form_submit_button(label="Login")
    back_button = st.form_submit_button(label="Back")

# Handle form submission
if submit_button:
    # Insert the user data into the database
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    st.success("Successfully submitted")

if back_button:
    st.write("Back button clicked")

# Close the database connection
conn.close()