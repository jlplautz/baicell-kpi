import  streamlit as st 
import pandas as pd

st.set_page_config(page_title="Solis KPI_Analysis", page_icon="📊")

st.markdown("SOLIS - KPI Analyis")
st.sidebar.header("SOLIS - KPI Analyis")
st.title(
    """This tool is going to be used to show the ENBs KPIs Performance."""
)


df = pd.read_csv("/mnt/c/Users/Jorge Luiz Plautz/Solis/KPIs/KPI_CloudCore_60Min-Mai24.csv")

df