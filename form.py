import streamlit as st

# Text Input
name = st.text_input("Enter your name")

# Number Input
number = st.number_input("Enter a number", min_value=1, max_value=100)

# Checkbox
agree = st.checkbox("I agree")

# Radio Button
gender = st.radio("Select Gender", ['Male', 'Female'])

# Dropdown Select Box
color = st.selectbox("Select a Color", ["Red", "Green", "Blue"])

# Multi-Select
skills = st.multiselect("Select Skills", ["Python", "SQL", "ML", "AI"])

# Button
if st.button("Submit"):
    st.success(f"Hello {name}, you selected {color} and {skills}")
