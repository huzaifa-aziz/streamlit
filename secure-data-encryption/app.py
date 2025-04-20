import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Generate a key (this would be fixed/stored securely in real app)
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# Global state
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}  # Format: {encrypted_text: {"encrypted_text": "...", "passkey": "hashed"}}

if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0

# Utility functions
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text, passkey):
    hashed_passkey = hash_passkey(passkey)
    for data in st.session_state.stored_data.values():
        if data["encrypted_text"] == encrypted_text and data["passkey"] == hashed_passkey:
            st.session_state.failed_attempts = 0
            return cipher.decrypt(encrypted_text.encode()).decode()
    st.session_state.failed_attempts += 1
    return None

# UI Pages
def home():
    st.title("🏠 Welcome to Secure Data Manager")
    st.markdown("Use this app to **securely store and retrieve sensitive data** with encryption 🔐.")

def store_data():
    st.title("📦 Store Data")
    data = st.text_area("Enter data to encrypt:")
    passkey = st.text_input("Set a passkey:", type="password")

    if st.button("Encrypt & Store"):
        if data and passkey:
            encrypted_text = encrypt_data(data)
            hashed_passkey = hash_passkey(passkey)
            st.session_state.stored_data[encrypted_text] = {
                "encrypted_text": encrypted_text,
                "passkey": hashed_passkey
            }
            st.success("✅ Data encrypted and stored successfully!")
            st.code(encrypted_text, language='text')
        else:
            st.error("⚠️ Both fields are required!")

def retrieve_data():
    st.title("🔍 Retrieve Data")
    encrypted_text = st.text_area("Enter the encrypted data:")
    passkey = st.text_input("Enter your passkey:", type="password")

    if st.button("Decrypt"):
        if encrypted_text and passkey:
            result = decrypt_data(encrypted_text, passkey)
            if result:
                st.success(f"✅ Decrypted Data: {result}")
            else:
                st.error(f"❌ Incorrect passkey! Attempts remaining: {3 - st.session_state.failed_attempts}")
                if st.session_state.failed_attempts >= 3:
                    st.warning("🔒 Too many failed attempts. Redirecting to login...")
                    st.experimental_set_query_params(page="Login")
                    st.experimental_rerun()
        else:
            st.error("⚠️ Both fields are required!")

def login_page():
    st.title("🔑 Reauthorization Required")
    master_pass = st.text_input("Enter master password:", type="password")

    if st.button("Login"):
        if master_pass == "admin123":  # In real apps, use hashed passwords + user auth
            st.session_state.failed_attempts = 0
            st.success("✅ Access restored. Redirecting...")
            st.experimental_set_query_params(page="Retrieve")
            st.experimental_rerun()
        else:
            st.error("❌ Incorrect master password!")

# Routing logic using sidebar
pages = {
    "Home": home,
    "Store Data": store_data,
    "Retrieve Data": retrieve_data,
    "Login": login_page
}

# Default page control
query_params = st.query_params
default_page = query_params.get("page", ["Home"])[0]

st.sidebar.title("📋 Navigation")
selection = st.sidebar.radio("Go to", list(pages.keys()), index=list(pages.keys()).index(default_page))

# Show selected page
pages[selection]()
