import streamlit as st
import pandas as pd
import os

# Set page config
st.set_page_config(page_title="Dashboard", layout="wide")

# Load CSS
def load_css(css_file):
    with open(css_file, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load Data
def load_data(file_path):
    if os.path.exists(file_path):
        return pd.read_csv(file_path)
    else:
        return pd.DataFrame()  # Return empty if file doesn't exist

# Load CSS
load_css("/Users/annliu/MobileApp/static/css/styles.css")

# Sidebar
st.sidebar.title("Dashboard Options")
selected_file = st.sidebar.selectbox("Select a File to View", ["/Users/annliu/MobileApp/data/benchmarkprems.csv", "/Users/annliu/MobileApp/data/uninsuredyoung.csv", "/Users/annliu/MobileApp/data/raw_data.csv"])
file_path = f"data/{selected_file}"

# Main Content
st.title("Data Dashboard")

# Read and Display Data
df = load_data(file_path)
if not df.empty:
    st.header(f"Data from {selected_file}")
    st.dataframe(df)

    # Example Visualization
    if len(df.columns) >= 2:
        st.header("Sample Visualization")
        st.bar_chart(df[df.columns[1]])
else:
    st.write("File not found or empty. Please select another file.")