import streamlit as st 
from openbb_terminal.sdk import openbb

def main():

    st.set_page_config(layout="wide")

    st.title("OpenBB Terminal")

    st.write(''' An example app showing how OPENBB works''')

    st.write(f"OpenBB version: {openbb.__version__}")


main()