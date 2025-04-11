
import streamlit as st
import re

# Function to evaluate password strength
def evaluate_password(password):
    score = 0
    level = "Too Weak"

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    if re.search(r"\d", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 1:
        level = "Weak"
    elif score == 2:
        level = "Moderate"
    elif score == 3:
        level = "Strong"
    elif score == 4:
        level = "Very Strong"

    return level, score

# Page title
st.set_page_config(page_title="Password Strength Checker", layout="centered")
st.title("Password Strength Checker")
st.write("Check how secure your password is based on common security rules.")

# Input field for password
user_password = st.text_input("Enter your password:", type="password")

# Show result if password is entered
if user_password:
    result, points = evaluate_password(user_password)
    st.subheader(f"Strength Level: {result}")
    st.progress(points / 4)
