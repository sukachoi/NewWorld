# 데이터를 불러오는 것이 목적
import ccxt
from datetime import datetime, timedelta
import pandas as pd

class DataLoader:
    def __init__(self):
        self.binance = ccxt.binance()
        self.market = 'BTC/USDT'
        self.periods = '5m'

    def get_origin_data(self):
        # 현재는 exchange가 바낸만 구현
        ohlcvs = self.binance.fetch_ohlcv(self.market, self.periods)
        # 일자, 시가, 고가, 저가, 종가, 거래량
        df = pd.DataFrame(ohlcvs, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
        df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
        df['datetime'] = pd.DatetimeIndex(df['datetime']) + timedelta(hours=9)
        df.set_index('datetime', inplace=True)
        df.reset_index(inplace=True)
        self.df = df
        return self.df


if __name__ == '__main__':
    a = DataLoader()
    df = a.get_origin_data()
    print(df)
