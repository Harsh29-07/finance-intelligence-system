def calculate_kpis(df):
    
    total_income = df[df['Type']=='Income']['Amount'].sum()
    
    total_expense = df[df['Type']=='Expense']['Amount'].sum()
    
    net_savings = total_income - total_expense
    
    return total_income, total_expense, net_savings