import clipboard
import random
import streamlit as st
import string

st.title("Password Generator using 🐍")
st.title("")

char = st.slider('Password length', 0, 25)

password = ''.join(random.choices(string.ascii_letters + string.digits, k=char))

st.subheader(password)
st.title("")
if st.button("Generate and Copy to clipboard"):
        clipboard.copy(password)
        st.success('Text copied to clipboard!')
