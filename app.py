from flask import Flask, request, jsonify, send_from_directory, render_template_string, session, redirect, url_for, render_template
from werkzeug.security import generate_password_hash, check_password_hash
import os
from datetime import datetime
import sqlite3
from cryptography.fernet import Fernet

app = Flask(__name__, static_folder='frontend', template_folder='frontend')

# Configurações
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_default_secret_key_for_development')
DATABASE = os.path.join(basedir, 'database.db')

# Admin credentials from environment variables
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'cauaregolindo')
ADMIN_PASSWORD_HASH = os.environ.get('ADMIN_PASSWORD_HASH', generate_password_hash('poxapoxa1@2A'))

# Encryption key from environment variable
ENCRYPTION_KEY = os.environ.get('ENCRYPTION_KEY', 'I-ZZIGr1eqPEzaPMVsFd48M67cv9cdNaRCda8lgc2Hw=')
fernet = Fernet(ENCRYPTION_KEY.encode())

def init_db():
    with app.app_context():
        db = sqlite3.connect(DATABASE)
        cursor = db.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS logs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                message TEXT NOT NULL
            )
        ''')
        db.commit()
        db.close()

# New route for contact form submissions
@app.route('/api/contact', methods=['POST'])
def contact_form_submit():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({'message': 'All fields are required.', 'category': 'danger'}), 400

    date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    encrypted_message = fernet.encrypt(message.encode()).decode()

    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute('INSERT INTO logs (date, name, email, message) VALUES (?, ?, ?, ?)', (date, name, email, encrypted_message))
    db.commit()
    db.close()

    return jsonify({'message': 'Your message has been sent successfully!', 'category': 'success'}), 200

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and check_password_hash(ADMIN_PASSWORD_HASH, password):
            session['logged_in'] = True
            return redirect(url_for('logs'))
        else:
            return 'Invalid credentials', 401
    return render_page('login')

@app.route('/logs')
def logs():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM logs')
    log_entries = cursor.fetchall()
    db.close()

    logs = []
    for entry in log_entries:
        decrypted_message = fernet.decrypt(entry[4].encode()).decode()
        logs.append({'id': entry[0], 'date': entry[1], 'name': entry[2], 'email': entry[3], 'message': decrypted_message})

    log_page_content = render_template('logs.html', logs=logs)
    return render_page('logs', page_content=log_page_content)

@app.route('/delete_logs', methods=['POST'])
def delete_logs():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    
    db = sqlite3.connect(DATABASE)
    cursor = db.cursor()
    cursor.execute('DELETE FROM logs')
    db.commit()
    db.close()
    
    return redirect(url_for('logs'))

# Function to render a page with the base template
def render_page(page_name, body_class='', page_content=None, **kwargs): # Added body_class parameter
    with open(os.path.join(app.template_folder, 'index.html'), 'r') as f:
        base_template = f.read()
    
    with open(os.path.join(app.template_folder, f'{page_name}.html'), 'r') as f:
        page_content = f.read()
    
    # Replace the content placeholder in the base template
    final_html = base_template.replace('<!-- Content will be loaded here by Flask -->', page_content)
    
    # Add body_class to the <body> tag
    if body_class:
        final_html = final_html.replace('<body>', f'<body class="{body_class}">')

    # Add login/logout link to the footer
    if session.get('logged_in'):
        final_html = final_html.replace('<!-- Add other social links here if desired -->', '<a href="/logout">Logout</a>')
    else:
        final_html = final_html.replace('<!-- Add other social links here if desired -->', '<a href="/login">Admin Login</a>')
    
    return render_template_string(final_html)

@app.route('/')
@app.route('/home')
def home_page():
    return render_page('home', body_class='home-page') # Added body_class

@app.route('/about')
def about_page():
    return render_page('about')

@app.route('/profile')
def profile_page():
    return render_page('profile')

@app.route('/services')
def services_page():
    return render_page('services')

@app.route('/repositories') # New route for repositories page
def repositories_page():
    return render_page('repositories')

@app.route('/contact')
def contact_page():
    return render_page('contact')

@app.route('/certificates')
def certificates_page():
    return render_page('certificates')

# Serve static files (CSS, JS, images)
@app.route('/<path:filename>')
def serve_static(filename):
    # Check if the file is in the frontend directory
    if os.path.exists(os.path.join(app.template_folder, filename)):
        return send_from_directory(app.template_folder, filename)
    # Check if the file is in the static directory (for hero_background.jpg)
    elif os.path.exists(os.path.join(basedir, 'static', filename)):
        return send_from_directory(os.path.join(basedir, 'static'), filename)
    # If not found in frontend or static, try to serve from frontend as a fallback
    return send_from_directory(app.template_folder, filename)


if __name__ == '__main__':
    init_db()
    app.run(debug=True)