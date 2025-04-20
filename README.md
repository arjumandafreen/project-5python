# 🔐 Secure Encryption App

A simple, user-friendly web application built with **Streamlit** that allows users to **store** and **retrieve encrypted data** securely. Ideal for managing sensitive personal notes, secrets, or credentials using custom passkeys.

## 🚀 Features

- 📝 **User Authentication** – Signup and login with secure password hashing.
- 📥 **Store Data** – Encrypt and save your private information using a custom passkey.
- 🔐 **Retrieve Data** – Decrypt and view stored data only with the correct passkey.
- 👮 **Security** – Includes limited login attempts and per-entry decryption protection.
- 🚪 **Logout System** – Secure session management.

---

## 📦 Requirements

- Python 3.7+
- Streamlit
- `utils.py` module (for encryption, decryption, and data persistence)

Install dependencies:

```bash
pip install streamlit
You also need to make sure your utils.py file includes functions like:

hash_password(password: str) -> str

encrypt(data: str) -> str

decrypt(encrypted_data: str) -> str

load_users() -> dict

save_users(users: dict)

load_data() -> dict

save_data(data: dict)

🛠️ How to Run
Clone the repository or copy the files into a project folder.

Make sure utils.py is present and contains the necessary helper functions.

Run the app with Streamlit:


streamlit run app.py
Replace app.py with the filename of your main script if different.

📂 Project Structure
pgsql
Copy
Edit
secure-encryption-app/
│
├── app.py           # Main Streamlit app
├── utils.py         # Helper functions (encryption, storage, hashing)
├── users.json       # Stored user credentials (hashed)
├── data.json        # Encrypted user data
└── README.md        # Project documentation
🔒 Security Note
This application is a demonstration tool and should not be used for storing highly sensitive data in production environments. For real-world applications, consider:

Using proper cryptographic libraries like Fernet from cryptography           https://project-5python-9twbh2xappvxcoavd5jrxn2.streamlit.app/

Implementing key management systems

Securing data storage with file encryption or databases

🧑‍💻 Author ARJUMAND AFREEN TABINDA
Built using Streamlit – a fast way to build data apps in Python.
