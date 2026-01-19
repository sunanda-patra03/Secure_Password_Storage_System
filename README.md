# 🔐 Secure Password Storage System (2025)

## 📌 Overview
This project is a Python-based authentication system that securely stores user passwords using **SHA-256 hashing** instead of plaintext credentials. It demonstrates secure authentication flow and fundamental cybersecurity best practices.

---

## 🚀 Features
- Secure password storage using SHA-256 hashing
- User registration and login functionality
- Password verification using hash comparison
- Avoids plaintext password storage
- Simple CLI-based interface

---

## 🛠 Tech Stack
- **Language:** Python 3
- **Security:** hashlib (SHA-256)
- **Storage:** JSON file
- **Concepts:** Authentication, Hashing, Credential Security

---

## 📂 Project Structure
Secure-Password-Storage-System/
│
├── auth.py # Handles user registration and login logic
├── hash_utils.py # Password hashing utility using SHA-256
├── main.py # Main program entry point
├── users.json # Stores hashed user credentials
├── requirements.txt # Project dependencies
└── README.md # Project documentation

---

## ▶ How to Run the Project

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/YOUR-USERNAME/Secure-Password-Storage-System.git

2️⃣ Navigate to the Project Directory
cd Secure-Password-Storage-System
3️⃣ Run the Application
python main.py

🔐 secure Password Storage System

1. Register
2. Login
3. Exit
