from flask import Flask, request, jsonify, send_from_directory, render_template_string
import os
from datetime import datetime

app = Flask(__name__, static_folder='frontend', template_folder='frontend')

# Configurações
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'a_default_secret_key_for_development')

# New route for contact form submissions
@app.route('/api/contact', methods=['POST'])
def contact_form_submit():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    message = data.get('message')

    if not name or not email or not message:
        return jsonify({'message': 'All fields are required.', 'category': 'danger'}), 400

    log_entry = f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] Name: {name}, Email: {email}, Message: {message}\n"
    
    try:
        with open(os.path.join(basedir, 'contact_log.txt'), 'a') as f:
            f.write(log_entry)
        return jsonify({'message': 'Your message has been sent successfully!', 'category': 'success'}), 200
    except Exception as e:
        print(f"Error writing to contact_log.txt: {e}")
        return jsonify({'message': 'Failed to send message. Please try again later.', 'category': 'danger'}), 500

# Function to render a page with the base template
def render_page(page_name, body_class=''): # Added body_class parameter
    with open(os.path.join(app.template_folder, 'index.html'), 'r') as f:
        base_template = f.read()
    
    with open(os.path.join(app.template_folder, f'{page_name}.html'), 'r') as f:
        page_content = f.read()
    
    # Replace the content placeholder in the base template
    final_html = base_template.replace('<!-- Content will be loaded here by Flask -->', page_content)
    
    # Add body_class to the <body> tag
    if body_class:
        final_html = final_html.replace('<body>', f'<body class="{body_class}">')
    
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
    app.run(debug=True)