import streamlit as st
import pandas as pd

raw_data = pd.read_csv("./NYPD_Complaint_Data.csv")

st.markdown("Data shape:")
st.write(raw_data.shape)

st.markdown("First 10 rows:")
st.dataframe(raw_data.head(10))

st.code("pandas.describe()")
st.write(raw_data.describe(include='all'))