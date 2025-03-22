import streamlit as st

# Title and Header
st.title("🌐 Streamlit Basics")
st.header("Hello, welcome to your first Streamlit app!")

# Text and Markdown
st.write("This is a simple web app built with Streamlit.")
st.markdown("**Streamlit makes web apps easy!**")

# User Input
name = st.text_input("Enter your name:")
st.write(f"Hello, {name} 👋")

# Slider
age = st.slider("Select your age", 0, 100)
st.write(f"You are {age} years old")

# Button
if st.button("Greet Me"):
    st.success(f"Hello, {name}! You are {age} years old.")
