import streamlit as st
import time
st.markdown("""
<style>
.stAppHeader.st-emotion-cache-h4xjwg.ezrtsby2
{
 visibility:hidden
}
</style>
""",unsafe_allow_html=True)
st.audio("audio1214378559.m4a")
st.video('video1214378559.mp4')
def change():
    print(st.session_state.checker)
state=st.checkbox("checkbox", value= True, on_change=change,key= 'checker')
radio_btn=st.radio('In which country do you live?', options=('Us','UK','Canada'))
print(radio_btn)
btn=st.button("click Me",on_click= 'btn_click')
select=st.selectbox('what is your favourite car?',options=('Audio','BMW','Feraari'))
print(select)
Multi_select=st.multiselect('what is your favourite Tech Brand',options=('Microsoft','Apple','Amazon','Oracle'))
print(Multi_select)
st.write(Multi_select)
