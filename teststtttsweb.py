import ST
import streamlit as st
st.write("Hello streamlit")
while True:
    #print("\n<---ฉันกำลังฟังคุณอยู่--->")
    text = ST.stt('th',2)
    #print("คุณพูดว่า --> ",text)
    st.write(text)
    if text == "สวัสดี":
        ST.tts("ฉันชื่อสมศรีค่ะ",'th')    


