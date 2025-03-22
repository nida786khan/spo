import streamlit as st
import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.sample(characters, length))

st.title("Secure Password Generator")

num_passwords = st.number_input("How many passwords?", min_value=1, value=5)
password_length = st.number_input("Password length:", min_value=4, value=8)

if st.button("Generate Passwords"):
    st.subheader("Your Secure Passwords:")
    for _ in range(num_passwords):
        st.code(generate_password(password_length))
