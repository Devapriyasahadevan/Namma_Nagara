# 🌆 Namma Nagara - Smart City Portal

**Namma Nagara** is a Python Flask web application that serves as a smart city portal for citizens to access city services, submit complaints, and contact departments. An admin dashboard is available to view all citizen complaints via secure login.

---

## 🗂️ Project Structure

namma_nagara/ ├── app.py ├── complaints.txt ├── templates/ │ ├── layout.html │ ├── index.html │ ├── services.html │ ├── complaints.html │ ├── contact.html │ ├── admin.html │ └── admin_login.html ├── static/ │ ├── css/style.css │ └── js/script.js └── README.md


---

## 🚀 Features

- 🏠 Home page with portal intro
- 🛠️ City services info
- 📝 Complaint submission form
- ☎️ Contact information
- 🔐 Admin login
- 📋 Admin dashboard to view complaints
- 💾 Complaints stored in a local text file (`complaints.txt`)

---

## 🔧 Technologies Used

- Python 3
- Flask
- HTML5
- CSS3
- JavaScript

---

## ✅ Requirements

Install Flask using pip:

```bash
pip install flask


cd namma_nagara
python app.py
http://127.0.0.1:5000/


http://127.0.0.1:5000/admin-login
Username	Password
admin	    admin123


Complaints are saved in a file named complaints.txt in the format:
User Name: Complaint Message