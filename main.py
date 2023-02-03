import pandas as pd
import numpy
import talib

close = numpy.random.random(100) * 100
output = talib.SMA(close)


def get_max_close(symbol):
    df = pd.read_csv(f'data/{symbol}.csv')
    return df['Close'].max()
    
    
if __name__ == '__main__':
    for symbol in ['AAPL', 'IBM']:
        print(get_max_close(symbol))


