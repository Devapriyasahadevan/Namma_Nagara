from flask import Flask, render_template, request, redirect, url_for, session, flash
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # change this in production

COMPLAINT_FILE = 'complaints.txt'
ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = 'admin123'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/complaints', methods=['GET', 'POST'])
def complaints():
    if request.method == 'POST':
        name = request.form['name']
        message = request.form['message']
        with open(COMPLAINT_FILE, 'a') as file:
            file.write(f"{name}: {message}\n")
        flash("Complaint submitted successfully.")
        return redirect(url_for('complaints'))
    return render_template('complaints.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin_logged_in'] = True
            return redirect(url_for('admin'))
        else:
            flash("Invalid credentials. Try again.")
    return render_template('admin_login.html')

@app.route('/admin')
def admin():
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))
    complaints_list = []
    if os.path.exists(COMPLAINT_FILE):
        with open(COMPLAINT_FILE, 'r') as file:
            complaints_list = file.readlines()
    return render_template('admin.html', complaints=complaints_list)

@app.route('/logout')
def logout():
    session.pop('admin_logged_in', None)
    return redirect(url_for('admin_login'))

@app.route('/delete/<int:index>', methods=['POST'])
def delete_complaint(index):
    if not session.get('admin_logged_in'):
        return redirect(url_for('admin_login'))

    if os.path.exists(COMPLAINT_FILE):
        with open(COMPLAINT_FILE, 'r') as file:
            complaints = file.readlines()

        if 0 <= index < len(complaints):
            complaints.pop(index)

            with open(COMPLAINT_FILE, 'w') as file:
                file.writelines(complaints)

    return redirect(url_for('admin'))


if __name__ == '__main__':
    app.run(debug=True)


