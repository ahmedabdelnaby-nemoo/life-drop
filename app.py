
from flask import Flask, render_template, request
import sqlite3
import os

app = Flask(__name__)

# Home Page
@app.route('/')
def home():
    return render_template("index.html")

# Show All Donors
@app.route('/show')
def show():

    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM donors")
    donors = cursor.fetchall()
    conn.close()
    return render_template("show.html", donors=donors)

# Donors Page
@app.route('/donors')
def donors():
    return render_template("donors.html")

# Save Donor
@app.route('/save', methods=['POST'])
def save():

    name = request.form['name']
    blood = request.form['blood']
    city = request.form['city']
    phone = request.form['phone']
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS donors(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            blood TEXT,
            city TEXT,
            phone TEXT
        )
    ''')

    cursor.execute('''
        INSERT INTO donors(name, blood, city, phone)
        VALUES (?, ?, ?, ?)
    ''', (name, blood, city, phone))

    conn.commit()
    conn.close()

    return render_template("success.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host="0.0.0.0", port=port, debug=False)