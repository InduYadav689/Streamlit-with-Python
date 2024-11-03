import streamlit as st
import datetime
st.markdown('<h1 style="text-align: center;">YSR CHEYUTHA 2023-2024 WFA/WWDS FIELD VERIFICATION FORM</h1>',unsafe_allow_html=True)
with st.form("form1",clear_on_submit=True):
    st.markdown('<h4>Secretariat Details</h4>',unsafe_allow_html=True)
    col1,col2=st.columns(2)
    col1.text_input("Secretariat Name ")
    col2.text_input(" Volunteer Name")
    col1.text_input("Secretariat Code")
    col2.text_input("Cluster ID")
    st.write('<h4>Applicant Basic Details</h4>',unsafe_allow_html=True)
    adhar=col1.text_input('Applicant ID')
    col2.text_input('Aadhar No')
    col1.text_input('Applicant Name')
    col2.text_input('Spouse Name')
    st.date_input('Date of birth')
    st.selectbox('Gender',options=('Male','Female'))
    st.text_input('Mobile No')
    st.markdown('<h4>Caste Details</h4>',unsafe_allow_html=True)
    st.text_input("Certification No")
    st.selectbox('Caste',options=('ST','SC','BC-A','BC-B','BC-C','BC-D','BC-E','OC'))
    st.text_input('Sub-caste')
    sub=st.form_submit_button('Submit')
    if sub:
        if adhar=="":
            st.warning('Please Fill above field')
        else:
            st.success('Submitted Sucessfully')
    