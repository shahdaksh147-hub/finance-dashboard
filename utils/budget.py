def check_budget(df, limit=10000):
    expense = df[df["Type"]=="Expense"]["Amount"].sum()
    
    if expense > limit:
        return f"⚠️ Budget exceeded! You spent ₹{expense}"
    else:
        return f"✅ Within budget. Total: ₹{expense}"
