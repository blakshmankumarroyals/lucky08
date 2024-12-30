import streamlit as st
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('personal_details.db')
c = conn.cursor()

# Create personal_details table if it doesn't exist
c.execute('''
    CREATE TABLE IF NOT EXISTS personal_details (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        address TEXT NOT NULL
    )
''')
conn.commit()

# Set the title of the app
st.title("Personal Details")

# Create a form for personal details
with st.form("personal_details_form"):
    name = st.text_input("Name", value="", max_chars=100)
    email = st.text_input("Email", value="", max_chars=100)
    phone = st.text_input("Phone", value="", max_chars=15)
    address = st.text_area("Address", value="", max_chars=500)
    
    # Add a submit button
    submit_button = st.form_submit_button(label="Submit")

# Handle form submission
if submit_button:
    # Insert the personal details into the database
    c.execute('INSERT INTO personal_details (name, email, phone, address) VALUES (?, ?, ?, ?)', (name, email, phone, address))
    conn.commit()
    st.success("Successfully submitted")

# Close the database connection
conn.close()