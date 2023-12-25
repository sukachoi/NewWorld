import datetime

from NewWorld.dataloader.DataLoader import DataLoader
from NewWorld.chartdrawer.ChartDrawer import ChartDrawer
import time

if __name__ == '__main__':

    a = DataLoader()
    b = ChartDrawer(a)
    b.plot_candlestick_chart()



#    data_loader = DataLoader()
#    chart_drawer = ChartDrawer(data_loader)
 #   chart_drawer.plot_candlestick_chart()
