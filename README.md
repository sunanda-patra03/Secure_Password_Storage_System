🔐 Secure Password Storage System


A Python-based authentication system that securely stores user passwords using SHA-256 hashing instead of plaintext. This project demonstrates secure login mechanisms and core cybersecurity best practices used in real-world applications.

📌 Overview

Storing passwords as plain text is a major security risk. This system prevents that by converting passwords into cryptographic hashes, ensuring that even if the data file is exposed, original passwords cannot be easily retrieved.

This project is ideal for beginners learning:

Authentication systems

Password security

Hashing algorithms

Secure coding practices

🚀 Features
```
✔ Secure password storage using SHA-256 hashing
✔ User registration and login system
✔ Password verification via hash comparison
✔ No plaintext password storage
✔ Lightweight JSON-based storage
✔ Simple command-line interface
```
🛠 Tech Stack

Component	Technology Used
Language	Python 3
Security	```hashlib``` (SHA-256)
Storage	JSON file
Concepts	Authentication, Hashing, Credential Security

📂 Project Structure

```
Secure-Password-Storage-System/
│
├── auth.py          # Handles user registration and login logic
├── hash_utils.py    # Password hashing utility using SHA-256
├── main.py          # Main program entry point
├── users.json       # Stores hashed user credentials
├── requirements.txt # Project dependencies
└── README.md        # Project documentation
```

▶ How to Run the Project

1️⃣ Clone the Repository

```
git clone https://github.com/YOUR-USERNAME/Secure-Password-Storage-System.git
```

2️⃣Navigate to the Project Directory

```
cd Secure-Password-Storage-System
```

3️⃣ Run the Application

```
python main.py
```

🔄 How It Works

User enters a password during registration.

The password is converted into a SHA-256 hash.

The hashed password is stored in users.json.

During login, the entered password is hashed again.

The system compares the new hash with the stored hash.

Access is granted only if both hashes match.


🔒 Why Hashing is Important

Protects user credentials

Prevents data leaks from exposing real passwords

Used in real systems like banking and web applications

Fundamental concept in cybersecurity


📚 Learning Outcomes


By building this project, you understand:

Secure authentication flow

Password hashing mechanisms

Data security fundamentals

How login systems work internally


⚠ Limitations (Future Improvements)


🔹 Add salting for stronger protection
🔹 Use a database instead of JSON storage
🔹 Implement password strength validation
🔹 Add GUI or web interface
🔹 Implement rate limiting against brute-force attacks


👨‍💻 Author

Sunanda Patra.

