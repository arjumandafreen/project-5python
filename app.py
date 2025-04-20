import streamlit as st
from utils import *

# Page config
st.set_page_config(page_title="🔐 Secure Encryption App", layout="centered", initial_sidebar_state="collapsed")

# Session state defaults
st.session_state.setdefault("logged_in", False)
st.session_state.setdefault("current_user", "")
st.session_state.setdefault("failed_attempts", 0)

# ---------- AUTH SYSTEM ----------
if not st.session_state.logged_in:
    st.title("🔐 Secure Data Encryption System")
    st.markdown("Welcome! Please choose an option below to continue.")

    auth_mode = st.radio("Select Mode", ["📝 Signup", "🔓 Login"], horizontal=True)

    if auth_mode == "📝 Signup":
        st.header("📝 Create Account")
        new_user = st.text_input("👤 New Username")
        new_pass = st.text_input("🔑 New Password", type="password")

        if st.button("✅ Signup"):
            if new_user and new_pass:
                users = load_users()
                if new_user in users:
                    st.warning("⚠️ Username already exists.")
                else:
                    users[new_user] = hash_password(new_pass)
                    save_users(users)
                    st.success("🎉 Account created! You can now log in.")
            else:
                st.warning("⚠️ Please fill in both fields.")

    else:
        st.header("🔓 Login to Your Account")
        user = st.text_input("👤 Username")
        pwd = st.text_input("🔑 Password", type="password")

        if st.button("🔐 Login"):
            users = load_users()
            if user in users and users[user] == hash_password(pwd):
                st.session_state.logged_in = True
                st.session_state.current_user = user
                st.session_state.failed_attempts = 0
                st.success("✅ Login successful!")
                st.rerun()
            else:
                st.error("❌ Invalid username or password.")

# ---------- MAIN APP ----------
if st.session_state.logged_in:
    username = st.session_state.current_user
    all_data = load_data()
    all_data.setdefault(username, [])
    user_data = all_data[username]

    st.sidebar.success(f"👋 Welcome, {username}")
    st.sidebar.markdown("## 🧰 Tools")
    choice = st.sidebar.radio("Navigate", ["🏠 Dashboard", "📥 Store Data", "🔐 Retrieve Data", "🚪 Logout"])

    # -- Dashboard
    if choice == "🏠 Dashboard":
        st.title("🏠 Dashboard")
        st.markdown(f"#### 👤 Logged in as: `{username}`")
        st.divider()
        st.markdown("### 🔧 Features")

        col1, col2 = st.columns(2)
        with col1:
            st.info("📥 Store sensitive information securely with encryption.")
        with col2:
            st.info("🔐 Retrieve and decrypt data using your passkey.")
        
        st.success("🔒 Your data is encrypted and safe!")

    # -- Store Data
    elif choice == "📥 Store Data":
        st.header("📥 Store Encrypted Data")
        user_input = st.text_area("🔒 Enter the data to encrypt")
        passkey = st.text_input("🔑 Create a passkey", type="password")

        if st.button("🛡️ Encrypt & Save"):
            if user_input and passkey:
                encrypted = encrypt(user_input)
                passkey_hash = hash_password(passkey)

                user_data.append({
                    "encrypted": encrypted,
                    "passkey": passkey_hash
                })

                save_data(all_data)
                st.success("✅ Data encrypted and saved securely!")
            else:
                st.warning("⚠️ Please fill in both fields.")

    # -- Retrieve Data
    elif choice == "🔐 Retrieve Data":
        st.header("🔐 Decrypt Your Stored Data")

        if not user_data:
            st.info("ℹ️ You have not stored any data yet.")
        else:
            for idx, item in enumerate(user_data):
                st.markdown(f"##### 🔐 Entry #{idx + 1}")
                st.code(item["encrypted"], language="text")

                input_passkey = st.text_input(f"🔑 Enter Passkey for Entry #{idx + 1}", type="password", key=f"pk_{idx}")
                if st.button(f"🔓 Decrypt Entry #{idx + 1}", key=f"decrypt_{idx}"):
                    if hash_password(input_passkey) == item["passkey"]:
                        decrypted = decrypt(item["encrypted"])
                        st.success(f"✅ Decrypted Data: {decrypted}")
                        st.session_state.failed_attempts = 0
                    else:
                        st.session_state.failed_attempts += 1
                        remaining = 3 - st.session_state.failed_attempts
                        st.error(f"❌ Incorrect passkey. Attempts left: {remaining}")

                        if st.session_state.failed_attempts >= 3:
                            st.warning("🔒 Too many failed attempts. You have been logged out.")
                            st.session_state.logged_in = False
                            st.session_state.current_user = ""
                            st.session_state.failed_attempts = 0
                            st.rerun()

    # -- Logout
    elif choice == "🚪 Logout":
        st.header("🚪 Logout")
        if st.button("✅ Confirm Logout"):
            st.session_state.logged_in = False
            st.session_state.current_user = ""
            st.success("👋 You have been logged out.")
            st.rerun()
