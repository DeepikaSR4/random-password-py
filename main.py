import random
import streamlit as st
import string

st.title("Password Generator using 🐍")
st.title("")

char = st.slider('Password length', 0, 25)
st.title("")
password = ''.join(random.choices(string.ascii_letters + string.digits, k=char))
if st.button("Generate"):
  st.subheader(password)
st.title("")

