import streamlit as st
from free_math_solver import solve_query

st.set_page_config(page_title="Free AI-Like Calculator", layout="centered")
st.title("🧮 free AI calculator")

user_input = st.text_input("Enter your math question (e.g., 'What is 25% of 640?'):")

if st.button("Calculate"):
    if user_input.strip():
        result = solve_query(user_input)
        st.success(f"✅ {result}")
    else:
        st.warning("Please enter a question.")
