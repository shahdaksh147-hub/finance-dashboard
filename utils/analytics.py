import streamlit as st

def show_charts(df):
    if df.empty:
        st.info("No data")
        return
    
    st.bar_chart(df.groupby("Category")["Amount"].sum())
