from bokeh.io import show
from bokeh.plotting import figure

from .base import Plotter


class TimeSeries(Plotter):
    def plot(self, **kwargs):
        # TODO: Check for invalid kwargs
        # TODO: Or let the parent parse the args

        self._read_data(index_name='dts',
                        index_col=kwargs['index_col'],
                        value_name='val',
                        value_col=kwargs['value_col'],
                        index_by_date_time=True)

        fig = figure(
            x_axis_type='datetime',
            title=self._data_file,
            plot_height=500,  # TODO: Expose as CLI parameter
            plot_width=1000  # TODO: Expose as CLI parameter
        )
        fig.xgrid.grid_line_color = None
        fig.ygrid.grid_line_alpha = 0.5
        fig.xaxis.axis_label = 'Date/Time'
        fig.yaxis.axis_label = 'Measurement Value'
        fig.background_fill_color = 'Beige'
        fig.background_fill_alpha = 0.5
        fig.line(self._data.index, self._data.val)

        show(fig)
