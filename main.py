# ROI por dia da semana
import pandas as pd
import yfinance as yf
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

df = yf.Ticker('BTC-USD').history(period='max').reset_index()
df = df[['Date', 'Open']]
df['Date'] = pd.to_datetime(df['Date'])

start = datetime(2021,1,1)
end = datetime.now()
dca = 100

df = df[df['Date'] >= start]

df['Compra'] = dca / df['Open'] # Checa quanto do ativo voce teria comprado no dia

df['Day Name'] = pd.to_datetime(df['Date']).dt.day_name()
df = df.groupby(df['Day Name']).sum() # Agrupa por dia da semana
print(df)

fig, ax = plt.subplots()
bar1 = ax.bar(df.index, df['Compra'])
ax.bar_label(bar1, padding=3)
ax.set_ylim(bottom = 0.95 * min(df['Compra']))

fig.suptitle('BTC adquirida por dia da semana de 2021 ate hoje')
plt.show()
