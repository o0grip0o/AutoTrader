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
def get_data(ticker: str, start: str, end: str) -> object:
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

def get_recommendations(predictions, portfolio):
    return {stock: ('Buy' if prediction > 0.5 else 'Sell') for stock, prediction in zip(portfolio, predictions)}

def get_portfolio():
    portfolio = {
        'LMC' : 10,
        'AMZN': 30
    }
    return portfolio

def get_trades(recommendations, portfolio):
    trades = []
    for stock, quantity in portfolio.items():
        if recommendations[stock] == 'Buy':
            trades.append((stock, 'Buy', quantity))
        elif recommendations[stock] == 'Sell':
            trades.append((stock, 'Sell', quantity))
    return trades

def main():
    # Get data
    data = get_data('AMZN', '2016-01-01', '2023-11-19')
    # Get model
    model = get_model((data.shape[1],))
    # Get predictions
    predictions = get_predictions(model, data)
    # Get portfolio
    portfolio = get_portfolio()
    # Get recommendations
    recommendations = get_recommendations(predictions, portfolio)
    # Get trades
    trades = get_trades(recommendations, portfolio)
    # Print trades
    print(trades)

if __name__ == '__main__':
    main()