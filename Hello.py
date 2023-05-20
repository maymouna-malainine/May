# simple app to test streamlit
import streamlit as st
st.title("Hello world!")
st.header("This is a header")
st.subheader("This is a subheader click here : https://www.youtube.com")
st.write("simple test for streamlit")
if st.button("Click Me"):
    st.write("you clicked me!")
    st.balloons()
    
st.sidebar.header("this is a sidebar")

# create a button in the sidebar
button= st.sidebar.button(label="Press me please")

if button:
    st.sidebar.write("Hello there")
    st.sidebar.balloons()

# create 2 columns(2) 
col1, col2 = st.columns([1,2])
col1.header("This is column 1")
col1.write("This is column 1")
col2.header("This is column 2")
col2.write("This is column 2")
#add a selectbox to the sidebar
option = st.selectbox('How would you like to be contacted',('Email', 'Home phone','Mobile phone'))
st.write('You selected :', option)
