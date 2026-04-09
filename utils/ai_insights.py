def generate_insights(df):
    if df.empty:
        return "No data available"

    food = df[df["Category"]=="Food"]["Amount"].sum()
    total = df["Amount"].sum()

    if total == 0:
        return "No spending detected"

    percent = (food / total) * 100

    if percent > 30:
        return f"⚠️ You spent {percent:.1f}% on food. Try reducing expenses."
    else:
        return "✅ Spending looks balanced."
