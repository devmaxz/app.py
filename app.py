import streamlit as st

import pandas as pd
import numpy as np

# Set page title
st.set_page_config(page_title="My Streamlit App", layout="wide")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Visualization", "About"])

# Home Page
if page == "Home":
    st.title("🏠 Welcome to My Streamlit App")
    st.write("Use the sidebar to navigate between pages.")

# Data Visualization Page
elif page == "Data Visualization":
    st.title("📊 Data Visualization")

    
    

# About Page
elif page == "About":
    st.title("ℹ️ About This App")
    st.write("This is a simple Streamlit app with navigation.")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Developed with ❤️ using Streamlit")
