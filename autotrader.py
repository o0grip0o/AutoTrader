import pandas as pds
import numpy as np
import tensorflow as tf
import yfinance as yf

###
# Autotrader
# TODO: Project will make automated trades based on a models predictions using Pandas and yfinance
# 1. Get data
# 2. Get model
# 3. Get predictions
# 4. Get recommendations
# 5. Get portfolio
# 6. Get trades
# 7. Main
###
def get_data(ticker, start, end):
    data = yf.download(ticker, start, end)
    return data

def get_model():
    ...

def get_predictions():
    ...

def get_recommendations():
    ...

def get_portfolio():
    ...

def get_trades():
    ...

def main():
    ...

if __name__ == '__main__':
    main()