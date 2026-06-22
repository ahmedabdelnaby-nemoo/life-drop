
from flask import Flask, render_template, request, redirect, make_response
import sqlite3
import os

app = Flask(__name__, static_folder='static', static_url_path='/static')

SPLASH_CACHE_HEADERS = {
    'Cache-Control': 'no-store, no-cache, must-revalidate, max-age=0',
    'Pragma': 'no-cache',
}


def _no_cache(response):
    for key, value in SPLASH_CACHE_HEADERS.items():
        response.headers[key] = value
    return response


# Splash Page - Logo (always first when opening the site root)
@app.route('/')
def home():
    response = make_response(render_template('splash.html'))
    return _no_cache(response)


# Main landing page
@app.route('/index')
def index():
    return render_template('index.html')


# Donors registration — after splash, landing page, or success screen
@app.route('/donors')
def donors():
    allowed_sources = ('splash', 'index', 'success')
    if request.args.get('from') not in allowed_sources:
        return redirect('/')
    return render_template('donors.html')


# Show All Donors
@app.route('/show')
def show():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM donors')
    donors_list = cursor.fetchall()
    conn.close()
    return render_template('show.html', donors=donors_list)


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

    return render_template('success.html')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)
