import streamlit as st
import pandas as pd

def filter_by_location (df, location):
    return df.loc[df['BORO_NM'] == location]

def print_dataframe (df):
    st.markdown("Data shape:")
    st.write(df.shape)
    st.markdown("First 10 rows:")
    st.dataframe(df.head(10))

st.markdown("""
# Evaluating Methods for Outlier Detection in NYC Crime Incidents
""")

raw_data = pd.read_csv("./NYPD_Complaint_Data.csv")

print_dataframe(raw_data)

st.code("pandas.describe()")
st.write(raw_data.describe(include='all'))

st.markdown("""
### Crime in Brooklyn
""")

brooklyn_crimes = filter_by_location(raw_data, 'BROOKLYN')

print_dataframe(brooklyn_crimes)

st.markdown("""
""")