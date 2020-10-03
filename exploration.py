import streamlit as st
import pandas as pd
import plotly.express as px

def parse_data(raw_data):
    raw_data['parsed_time'] = pd.to_datetime(raw_data['CMPLNT_FR_DT'], errors='coerce')
    parsed_data = raw_data.set_index('parsed_time')
    return parsed_data[parsed_data.index.year == 2020]

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

parsed_data = parse_data(raw_data)

st.markdown("""
### Filter Crimes by Location
""")

location = st.selectbox("Select location", parsed_data['BORO_NM'].unique())
location_crimes = filter_by_location(parsed_data, location)

counts = location_crimes.groupby(['parsed_time']).agg(len)

fig = px.line(counts, y="CMPLNT_NUM", labels=["Test", "be"])
fig.update_xaxes(title="Time of complaint")
fig.update_yaxes(title="Number of complaints")
st.plotly_chart(fig)

st.markdown('#### Crimes in {}'.format(location))
print_dataframe(location_crimes)

st.markdown("""
""")

