import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Streamlit app
st.title("Milk Production Analysis")

# File upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the CSV file, making sure to handle headers correctly
    df = pd.read_csv(uploaded_file, header=0)
    
    # Show dataframe
    st.write("### Data Preview:")
    st.write(df.head())
    
    # Displaying the columns available in the dataset
    st.write("### Dataset Columns:")
    st.write(df.columns.tolist())
    
    # Check if 'Month' and 'Production' columns exist
    if 'Month' in df.columns and 'Production' in df.columns:
        # Convert 'Month' to datetime for better plotting
        df['Month'] = pd.to_datetime(df['Month'], errors='coerce')
        
        # Plot milk production trends
        st.write("### Milk Production Trends:")
        fig, ax = plt.subplots()
        ax.plot(df['Month'], df['Production'], label='Milk Production')
        ax.set_xlabel('Month')
        ax.set_ylabel('Milk Production (Pounds)')
        ax.legend()
        st.pyplot(fig)
    else:
        st.write("Error: The dataset must contain 'Month' and 'Production' columns.")
else:
    st.write("Please upload a CSV file to proceed.")
