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

def get_model(input_shape):
    model = tf.keras.models.Sequential([
        tf.keras.layers.Dense(32, activation='relu', input_shape=input_shape),
        tf.keras.layers.Dense(32, activation='relu'),
        tf.keras.layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def get_predictions(model, data):
    predictions = model.predict(data)
    return predictions

def get_recommendations():
    recommendations = ['Buy', 'Sell', 'Hold']
    return recommendations

def get_portfolio():
    ...

def get_trades():
    ...

def main():
    ...

if __name__ == '__main__':
    main()