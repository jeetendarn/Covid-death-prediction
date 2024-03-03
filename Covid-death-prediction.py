import pandas as pd
import numpy as np
data = pd.read_csv("COVID19 data for overall INDIA.csv")
print(data.head())
data.isnull().sum()
data = data.drop("Date", axis=1)
import plotly.express as px
fig = px.bar(data, x='Date_YMD', y='Daily Confirmed')
fig.show()
cases = data["Daily Confirmed"].sum()
deceased = data["Daily Deceased"].sum()

labels = ["Confirmed", "Deceased"]
values = [cases, deceased]

fig = px.pie(data, values=values, 
             names=labels, 
             title='Daily Confirmed Cases vs Daily Deaths', hole=0.01)
fig.show()
death_rate = (data["Daily Deceased"].sum() / data["Daily Confirmed"].sum()) * 100
print(death_rate)
import plotly.express as px
fig = px.bar(data, x='Date_YMD', y='Daily Deceased')
fig.show()
from AutotS import AutoTS
model = AutotS(forecast_length=30, frequency='infer', ensemble='simple')
model = model.fit(data, date_col="Date_YMD", value_col='Daily Deceased', id_col=None)
forecast = prediction.forecast
print(forecast)
