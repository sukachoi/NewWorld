import datetime

from dataloader.DataLoader import DataLoader
from chartdrawer.ChartDrawer import ChartDrawer #from 상위폴더.하위폴더 import 클래스이름
import time

if __name__ == '__main__':

    while True:
        a = DataLoader()
        df = a.get_origin_data()
        b = ChartDrawer(a)
        b.plot_candlestick_chart()
        time.sleep(60)



#    data_loader = DataLoader()
#    chart_drawer = ChartDrawer(data_loader)
 #   chart_drawer.plot_candlestick_chart()
