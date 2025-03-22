import streamlit as st

st.title("📊 Simple Web App")
st.write("Hello, this is your first Streamlit app!")

value = st.slider("Select a number", 0, 100)
st.write("You selected:", value)
