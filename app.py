import streamlit as st
import re

def check_password_strength(password):
    strength = 0
    if len(password) >= 8:
        strength += 1
    if re.search(r'[A-Z]', password):
        strength += 1
    if re.search(r'[a-z]', password):
        strength += 1
    if re.search(r'[0-9]', password):
        strength += 1
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength == 3:
        return "Moderate"
    else:
        return "Strong"

st.title("Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    strength = check_password_strength(password)
    st.write(f"Password Strength: **{strength}**")
else:
    st.write("Please enter a password to check its strength.")