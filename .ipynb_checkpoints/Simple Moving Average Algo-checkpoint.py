import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import yfinance as yf

#download three years of apple data from api
aapl = yf.download('AAPL', start='2020-01-01', end='2023-01-01')

print(aapl.head())
