import datetime

from NewWorld.dataloader.DataLoader import DataLoader
from NewWorld.chartdrawer.ChartDrawer import ChartDrawer
import time
from NewWorld.version import version
print("NewWord program version is " + str(version))

if __name__ == '__main__':

    data = input("원하는 코인 또는 주식을 입력해 주세요..ex: 'BTC/USDT', 'ETH/USDT', 'AAPL', '005930.KS'")
    print("")
    #coin = ['BTC/USDT', 'ETH/USDT']
    #stock = ['AAPL', '005930.KS']
    a = DataLoader(data)

    if 'USDT' in data:
        a.get_coin_data()
    else:
        a.get_stock_data()

    b = ChartDrawer(a)
    b.plot_candlestick_chart()


    #### 1~4 입력을 하세요.
    #사람한테 입력을 받는다. 1.비트코인, 2. 이더리움 3.삼성 4.애플

    #

#    data_loader = DataLoader()
#    chart_drawer = ChartDrawer(data_loader)
 #   chart_drawer.plot_candlestick_chart()
