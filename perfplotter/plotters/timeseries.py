from bokeh.io import show
from bokeh.plotting import figure

from .base import Plotter


class TimeSeries(Plotter):
    def __init__(self, data_file):
        super().__init__(data_file)

    def plot(self):
        self._read_data("time", "value", index_by_date_time=True)
        fig = figure(
            x_axis_type="datetime",
            title="",
            plot_height=500,  # TODO: Expose as CLI parameter
            plot_width=1000   # TODO: Expose as CLI parameter
        )
        fig.xgrid.grid_line_color = None
        fig.ygrid.grid_line_alpha = 0.5
        fig.xaxis.axis_label = "Time"
        fig.yaxis.axis_label = "Value"
        fig.background_fill_color = "Beige"
        fig.background_fill_alpha = 0.5
        fig.line(self._data.index, self._data.value)
        show(fig)
