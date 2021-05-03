import numpy as np
import pandas as pd
from bokeh.io import show
from bokeh.models import ColumnDataSource, HoverTool
from bokeh.plotting import figure

from .base import Plotter


class Histogram(Plotter):
    def plot(self, **kwargs):
        # TODO: Check for invalid kwargs
        # TODO: Or let the parent parse the args

        self._read_data(index_name='dts',
                        index_col=kwargs['index_col'],
                        value_name='val',
                        value_col=kwargs['value_col'],
                        index_by_date_time=True)

        # TODO: Expose the bins as CLI parameter
        # TODO: The density here means 'probability density', can we use this?
        hist, edges = np.histogram(self._data['val'], bins=20, density=False)

        hist_annotated = pd.DataFrame({
            'val': hist,  # Bucket value
            'min': edges[:-1],  # All the minimum edges of all the buckets
            'max':
                edges[1:]  # All the maxmimum edges of all the buckets
        })
        minmax = zip(hist_annotated['min'], hist_annotated['max'])
        hist_annotated['distribution'] = ['%.2f to %.2f' % (min, max) for min, max in minmax]
        hist_annotated['percentage'] = [100.0 * (val / self._data.size) for val in hist_annotated['val']]

        source = ColumnDataSource(hist_annotated)

        fig = figure(
            title=self._data_file,
            plot_height=500,  # TODO: Expose as CLI parameter
            plot_width=1000,  # TODO: Expose as CLI parameter
            x_axis_label='Distribution',
            y_axis_label='Percentage')
        fig.background_fill_color = 'Beige'
        fig.background_fill_alpha = 0.5
        fig.quad(
            source=source,
            bottom=0,
            top='percentage',
            left='min',
            right='max',
            fill_color='CornflowerBlue',
            fill_alpha=0.8,
            line_color='Black',
            hover_fill_alpha=1.0,  # Completely hide the original fill color
            hover_fill_color='Chocolate')

        hover = HoverTool(tooltips=[('Distribution', '@distribution'), ('Percentage', '@percentage')])
        fig.add_tools(hover)

        show(fig)
