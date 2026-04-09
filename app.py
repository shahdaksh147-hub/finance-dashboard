import streamlit as st
import pandas as pd
from utils.analytics import show_charts
from utils.ai_insights import generate_insights
from utils.budget import check_budget

st.set_page_config(page_title="Finance Dashboard", layout="wide")

st.title("💸 Finance Wellbeing Dashboard")

# Load data
try:
    df = pd.read_csv("data/transactions.csv")
except:
    df = pd.DataFrame(columns=["Type", "Category", "Amount", "Date"])

# Add transaction
st.sidebar.header("➕ Add Transaction")
t_type = st.sidebar.selectbox("Type", ["Income", "Expense"])
category = st.sidebar.text_input("Category")
amount = st.sidebar.number_input("Amount", min_value=0.0)
date = st.sidebar.date_input("Date")

if st.sidebar.button("Add"):
    new = pd.DataFrame([[t_type, category, amount, date]],
                       columns=df.columns)
    df = pd.concat([df, new], ignore_index=True)
    df.to_csv("data/transactions.csv", index=False)
    st.sidebar.success("Added!")

# Summary
income = df[df["Type"]=="Income"]["Amount"].sum()
expense = df[df["Type"]=="Expense"]["Amount"].sum()
balance = income - expense

col1, col2, col3 = st.columns(3)
col1.metric("💰 Income", f"₹{income}")
col2.metric("💸 Expense", f"₹{expense}")
col3.metric("🏦 Balance", f"₹{balance}")

# Charts
st.subheader("📊 Analytics Dashboard")
show_charts(df)

# AI Insights
st.subheader("🤖 AI Insights")
st.write(generate_insights(df))

# Budget Alerts
st.subheader("🎯 Budget Alerts")
st.write(check_budget(df))
