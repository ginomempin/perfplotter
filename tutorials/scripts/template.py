"""Bokeh Visualization Template"""

import pandas as pd
import numpy as np

from bokeh.io import output_file, output_notebook
from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import row, column, gridplot
from bokeh.models.widgets import Tabs, Panel

# STEP 1 - Get/Prepare the data

# STEP 2 - Determine where the visualization will be rendered
#   For static HTML / frontend
output_file('filename.html')
#   For Jupyter Notebook
output_notebook()

# STEP 3 - Setup the figure(s)
fig = figure()

# STEP 4 - Plot the data

# STEP 5 - Organize the layout

# STEP 6 - Preview and save
show(fig)
