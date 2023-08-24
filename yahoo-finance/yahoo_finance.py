import pandas as pd
import plotly.express as px

df = pd.read_csv("MSFT.csv")

# print(df.head())

fig = px.line(x=df['Date'], y=df['Adj Close'])
fig.show()