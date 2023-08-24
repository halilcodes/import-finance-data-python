import pandas as pd
import plotly.express as plt

df = pd.read_csv("MSFT.csv")

print(df.head())

plt.line(x=df['Date'], y=df['Close'])
