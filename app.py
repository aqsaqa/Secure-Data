import streamlit as st
from encryption_utils import encrypt_message, decrypt_message

st.set_page_config(page_title="Secure Data Encryption", layout="centered")

st.title("🔐 Secure Data Encryption App")
st.write("Encrypt and decrypt your text securely using AES-based Fernet encryption.")

mode = st.radio("Select Mode:", ["Encrypt", "Decrypt"])

if mode == "Encrypt":
    plain_text = st.text_area("Enter text to encrypt:")
    if st.button("Encrypt"):
        if plain_text.strip() == "":
            st.warning("Please enter some text.")
        else:
            encrypted = encrypt_message(plain_text)
            st.success("Encrypted Text:")
            st.code(encrypted, language="text")

elif mode == "Decrypt":
    encrypted_text = st.text_area("Enter encrypted text to decrypt:")
    if st.button("Decrypt"):
        try:
            decrypted = decrypt_message(encrypted_text)
            st.success("Decrypted Text:")
            st.code(decrypted, language="text")
        except Exception as e:
            st.error("Decryption failed! Please check the input.")
