import streamlit as st

st.title("welcome to giit computer")


name = st.text_input("enter your name:")
fname=st.text_input("enter your father name:")
adr=st.text_area("enter your text:")
classdata = st.selectbox("select your class:",(1,2,3,4,5))

button = st.button("done")
if button :
    st.markdown(f"""
       name :{name}
       father name :{fname}
       address : {adr}
       class :{classdata}""")