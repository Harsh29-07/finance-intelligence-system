from prophet import Prophet

def forecast_expenses(monthly_expense):
    
    model = Prophet()
    
    model.fit(monthly_expense)
    
    future = model.make_future_dataframe(
        periods=6,
        freq='MS'
    )
    
    forecast = model.predict(future)
    
    return forecast, model