'''Build a Password Strength Meter in Python that evaluates a user's password based on security rules. The program will:

Analyze passwords based on length, character types, and patterns.
Assign a strength score (Weak, Moderate, Strong).
Provide feedback to improve weak passwords.
Use control flow, type casting, strings, and functions.

🔹 Requirements
1. Password Strength Criteria
A strong password should:
✅ Be at least 8 characters long
✅ Contain uppercase & lowercase letters
✅ Include at least one digit (0-9)
✅ Have one special character (!@#$%^&*)

2. Scoring System
Weak (Score: 1-2) → Short, missing key elements
Moderate (Score: 3-4) → Good but missing some security features
Strong (Score: 5) → Meets all criteria


3. Feedback System
If the password is weak, suggest improvements.
If the password is strong, display a success message.
'''






import re
import streamlit as st

#page_styling
st.set_page_config(page_title="Password Strenght Checker, created by by M.Bin Aslam", page_icon="🔑", layout="centered")

#custom css
st.markdown(""""
<style>
    .main {
            text-align: center;}
    .stTextInput {
            width: 70% !important; 
            margin: auto;
            } 
    .stButton button {
            display: block;
            background-color: blue;
            color: white; 
            margin-left: auto;
            margin-right: auto;
            font-size: 18px
            padding: 10px 20px;
            width: 50%; 
            transition: background-color 0.3s, color 0.3s;
            }                 
    .stButton button:hover {
            background-color: red; 
            color: white;
            width: 50%; 
            }
</style>            
""", unsafe_allow_html=True)

#page title & description
# Inline CSS for centering the title
st.markdown("<h1 style='text-align: center;'>🔒 Password Strength Generator</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Enter your password below to check its security level:</h5>", unsafe_allow_html=True)


#function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1    #increased score by one
    else:
        feedback.append("❌ Password should be **atleast 8 characters long**")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain **both upper case{i.e.(A-Z)} and lower case{i.e.(a-z)}letters**.")

    if re.search(r"\d",password):
        score += 1
    else:
        feedback.append("❌ Password should contain atleast one number(i.e.0-9).")

    #special characters
    if re.search(r"[!@#$%^&*]",password):
        score += 1
    else:
        feedback.append("❌ Include **at least one special character(i.e.!@#$%^&*)**.")

    #display password strength results
    if score == 4: 
        st.success("✅ **Strong password - Your password is secure.**")
    elif score == 3:
        st.info("⚠️ **Moderate password - Consider improving by adding more features.**")
    else:
        st.error("❌ **Weak password - Try improving by following the suggestions below.**")

#feedback
    if feedback:
        with st.expander("🔁 **Improve Your Password**"):
            for item in feedback:
                st.write(item)
password = st.text_input("Enter your password:",type= "password",help="🔐 Ensure your password is strong." )

#button working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first.") #show warning if password is empty

