import plotly.graph_objects as go
from NewWorld.dataloader.DataLoader import DataLoader

class ChartDrawer:
    def __init__(self, data_loader):
        self.data_loader = data_loader


    def plot_candlestick_chart(self):
        #df = self.data_loader.get_origin_data()
        df = self.data_loader.df

        print("Starting Draw Chart....")
        fig = go.Figure(data=[go.Candlestick(x=df['datetime'],
                                             open=df['open'],
                                             high=df['high'],
                                             low=df['low'],
                                             close=df['close'])])

        print("Set Data....")
        fig.update_layout(title='Candlestick Chart for ' + self.data_loader.market, xaxis_title='Date', yaxis_title='Price')
        print("Update layout...")
        fig.show()
        print("Show Chart")


if __name__ == '__main__':
    data_loader = DataLoader()
    chart_drawer = ChartDrawer(data_loader, "apple")
    chart_drawer.plot_candlestick_chart()
