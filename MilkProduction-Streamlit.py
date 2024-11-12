import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit app
st.title("Milk Production Analysis")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file
    df = pd.read_csv(uploaded_file)
    
    # Show dataframe
    st.write("### Data Preview:")
    st.write(df.head())
    
    # Plot milk production trends
    st.write("### Milk Production Trends:")
    fig, ax = plt.subplots()
    ax.plot(df['Date'], df['Milk Production'], label='Milk Production')
    ax.set_xlabel('Date')
    ax.set_ylabel('Milk Production')
    ax.legend()
    st.pyplot(fig)
else:
    st.write("Please upload a CSV file to proceed.")
