import streamlit as st
from PIL import Image
from PIL.ImageFilter import *

st.markdown('<h1 style="text-align:center"> IMAGE EDITOR</h1>',unsafe_allow_html=True)
st.markdown('---')
image=st.file_uploader('upload your files',type=['png','jpg','pdf'])

if image:
    img=Image.open(image)
    st.image(img,caption='My Linkedin Image')
    st.write('size :',img.size)
    st.write('mode :',img.mode)
    st.write('format :',img.format)
    st.markdown('<h2 style="text-align: center">RESIZING</h2>',unsafe_allow_html=True)
    width=st.number_input("width",value=img.width)
    height=st.number_input("height",value=img.height)
    st.markdown('<h2 style="text-align: center">Rotation</h2>',unsafe_allow_html=True)
    degree=st.number_input('degree')
    st.markdown('<h2 style="text-align: center">Filters</h2>',unsafe_allow_html=True)
    filters=st.selectbox("Filters",options=('None','Blur','details','emboss','smooth'))
    st_btn=st.button('Submit')
    if st_btn:
        editor=img.resize((width,height)).rotate(degree) 
        filtered=editor
        if filters !='None':
            if filters=='Blur':
                filtered1=editor.filter(BLUR)
            elif filters == 'Details':
                filtered1=editor.filter(DETAIL)
            elif filters== 'emboss':
                filtered1=editor.filter(EMBOSS)
            else:
                filtered1=editor.filter(SMOOTH)
        st.image(filtered1)