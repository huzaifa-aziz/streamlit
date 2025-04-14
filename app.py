import streamlit as st
import string

SPECIAL_CHARACTERS = "!@#$%^&*"


def evaluate_password(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("🔸 Make your password at least 8 characters long.")


    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("🔸 Include at least one uppercase letter.")

    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("🔸 Include at least one lowercase letter.")

    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("🔸 Add at least one number (0–9).")

    if any(c in SPECIAL_CHARACTERS for c in password):
        score += 1
    else:
        feedback.append("🔸 Use at least one special character (!@#$%^&*).")

    return score, feedback


def strength_label(score):
    if score <= 2:
        return "❌ Weak", "red"
    elif 3 <= score <= 4:
        return "⚠️ Moderate", "orange"
    else:
        return "✅ Strong", "green"



st.title("password strength meter")

password = st.text_input("Enter Password: ", type = "password")

if password:
    score, feedback = evaluate_password(password)
    label, color = strength_label(score)

    st.markdown(f"### Strength: <span style='color:{color}'>{label}</span>", unsafe_allow_html=True )

    if score < 5:
        st.subheader("suggestions to improve:")
        for tip in feedback:
            st.write(tip)
        else:
            st.success("your password is strong! great job")