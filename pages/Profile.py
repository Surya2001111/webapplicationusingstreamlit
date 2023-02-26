import streamlit as st
import os
import base64
from PIL import Image


st.set_page_config(page_title='My Streamlit Portfolio')

image = Image.open('pic.jpg')
col1,col2= st.columns(2)
with col1:
    st.title("Suryakanta Sundaray")
    st.write("intern at Innomatics_Research_Lab")
    st.write("Data Science Enthusiastic")
    st.header('Contact')
    st.write('Email: suryakantasundaray20@.com')
    st.write('LinkedIn: https://www.linkedin.com/in/suryakanta-sundaray-14b9a0223/')
    st.write('instagram: https://www.instagram.com/bss__17/')
with col2:
    st.image(image, caption='Surya')

def show_pdf(file_path):
    with open(file_path,"rb") as f:
        base64_pdf = base64.b64encode(f.read()).decode('utf-8')
    pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
    st.markdown(pdf_display, unsafe_allow_html=True)



st.header('Projects')


st.subheader('Project 1: Cricket Score Prediction')
st.subheader('Project 2: NLP based web app using flask')
st.subheader('Project 3: Olympic story making using tableau')


st.header('Resume')

show_pdf("Resume Updated surya.pdf")