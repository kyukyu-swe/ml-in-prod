import yfinance as yf
import matplotlib.pyplot as plt

data = yf.download("TSLA GOOG", period="1mo")
print(type(data))
print(data.Close)

data.Close.plot()
plt.show()