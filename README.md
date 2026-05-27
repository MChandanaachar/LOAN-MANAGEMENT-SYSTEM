# 💰 Loan Management System

A full-stack Loan Management System built using **Flask (Backend)** and **HTML, CSS, JavaScript (Frontend)**.  
The project supports authentication, loan CRUD operations, and is fully deployed.

---

## 🚀 Live Demo

🔗 Frontend (Vercel):  
https://your-vercel-link.vercel.app

🔗 Backend API (Render):  
https://loan-management-system-7f0b.onrender.com

---

## 📌 Features

- User Login with JWT Authentication
- Add new loan details
- View all loans
- Edit loan details
- Delete loans
- Secure API with token-based authentication
- Fully responsive UI
- Connected frontend and backend via REST API

---

## 🛠️ Tech Stack

**Frontend:**
- HTML
- CSS
- JavaScript

**Backend:**
- Flask
- Flask-JWT-Extended
- Flask-CORS
- SQLAlchemy

**Database:**
- SQLite

**Deployment:**
- Frontend: Vercel
- Backend: Render

---

## 📂 Project Structure

loan-management-system/
│
├── backend/
│ ├── app.py
│ ├── config.py
│ ├── models.py
│ ├── routes.py
│ ├── requirements.txt
│
├── frontend/
│ ├── index.html
│ ├── style.css
│ ├── app.js
│ ├── assets/
│
└── README.md


---

## 🔐 Authentication Flow

- User logs in with username & password
- Backend returns JWT token
- Token is stored in localStorage
- Token is used for all protected API requests

---

## 📸 UI Preview

(Add screenshot here if you want later)

---

## ⚙️ How to Run Locally

### Backend
```bash
cd backend
pip install -r requirements.txt
python app.py

Frontend

Just open:

index.html
🌐 API Endpoints
Method	Endpoint	Description
POST	/login	User login
GET	/loans	Get all loans
POST	/loans	Add loan
PUT	/loans/<id>	Update loan
DELETE	/loans/<id>	Delete loan
👨‍💻 Author
M Chandana
Project: Loan Management System
⭐ Note

This project was built as a full-stack project to understand REST APIs, authentication, and deployment.

project deployment links==>

✔ Vercel frontend URL : loan-management-system-hycbj2lgg-m-chandana-s-projects.vercel.app
✔ Render backend URL  : https://loan-management-system-7f0b.onrender.com
