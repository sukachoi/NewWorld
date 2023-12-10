import plotly.graph_objects as go
from NewWorld.dataloader.dataloader import DataLoader

class ChartDrawer:
    def __init__(self, data_loader):
        self.data_loader = data_loader

    def plot_candlestick_chart(self):
        df = self.data_loader.get_origin_data()

        fig = go.Figure(data=[go.Candlestick(x=df.index,
                                             open=df['open'],
                                             high=df['high'],
                                             low=df['low'],
                                             close=df['close'])])

        fig.update_layout(title='Candlestick Chart for BTC/USDT',
                          xaxis_title='Date',
                          yaxis_title='Price')

        fig.show()

if __name__ == '__main__':
    data_loader = DataLoader()
    chart_drawer = ChartDrawer(data_loader)
    chart_drawer.plot_candlestick_chart()
