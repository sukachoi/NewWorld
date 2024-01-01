# 데이터를 불러오는 것이 목적
import ccxt
import yfinance as yf
from datetime import datetime, timedelta
import pandas as pd
from pandas_datareader import data as pdr
import matplotlib.pyplot as plt

class DataLoader:
    def __init__(self, data):
        self.binance = ccxt.binance()
        self.market = data
        self.periods = '1m'
        self.yf = yf.pdr_override()
        # 주식 코드와 기간 설정
        self.stock_code = 'apple'
        self.start_date = datetime(2022, 1, 1)
        self.end_date = datetime(2022, 12,31)
        self.interval = '1m'
        #self.get_stock_data()
        #self.get_coin_data()
        # Yahoo Finance에서 데이터 가져오기


    def get_coin_data(self):
    #####
         #현재는 exchange가 바낸만 구현
        ohlcvs = self.binance.fetch_ohlcv(self.market, self.periods)
        # 일자, 시가, 고가, 저가, 종가, 거래량
        df = pd.DataFrame(ohlcvs, columns=['datetime', 'open', 'high', 'low', 'close', 'volume'])
        df['datetime'] = pd.to_datetime(df['datetime'], unit='ms')
        df['datetime'] = pd.DatetimeIndex(df['datetime']) + timedelta(hours=9)
        df.set_index('datetime', inplace=True)
        df.reset_index(inplace=True)
        self.df = df

        print("비트코인...... 데이터 모양...")
        print(self.df)

        return self.df

    def get_stock_data(self):
        sec = pdr.get_data_yahoo(self.market, start='2023-01-01')
        #불필요 컬럼 삭제
        sec.drop(['Adj Close'], axis=1, inplace=True)
        #컬럼을 새로 만드는거
        sec['datetime'] = sec.index
        #컬럼 이름을 변경하기
        sec.columns= ['open', 'high', 'low', 'close','volume','datetime']
        #인덱스 삭제
        sec = sec.reset_index()
        #컬럼순서 변경
        sec = sec[['datetime', 'open', 'high', 'low', 'close', 'volume']]
        self.df = sec
        print("야후...... 데이터 모양...")
        print(self.df)


        return self.df




if __name__ == '__main__':


    data = input("원하는 코인 또는 주식을 입력해 주세요")
    coin = ['btc']
    stock = ['apple']
    a = DataLoader(data)
    if data in coin:
        df = a.get_coin_data()
    if data in stock:
        df = a.get_stock_data()
    print(df)
