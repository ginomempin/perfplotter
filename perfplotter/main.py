import click

from .examples import gaussian
from .plotters import Histogram, TimeSeries

# ------------------------------------------------------------------------------
# CLI commands for plotting
# ------------------------------------------------------------------------------


@click.group()
def plot_cmds():
    pass


@plot_cmds.command(short_help='Show a time series plot')
@click.argument('filename')
@click.option('-x', 'dts_idx', default=0, show_default=True, type=int, help='0-based index of the Date/Time')
@click.option('-y', 'val_idx', default=1, show_default=True, type=int, help='0-based index of the Measurement Value')
def timeseries(filename, dts_idx, val_idx):
    """
    Generates a timeseries plot using the data from FILENAME.csv.

    The plotter uses the Date/Time column for the X-axis and the
    measurement value for the Y-axis. It assumes column=0 to be
    the Date/Time column and column=1 to be the measurement value
    column. Pass in --dts and --val to specify different indices.

    The plotter currently does not support CSV with headers.
    """
    plotter = TimeSeries(filename)
    plotter.plot(index_col=dts_idx, value_col=val_idx)


@plot_cmds.command(short_help='Show a histogram plot')
@click.argument('filename')
@click.option('-x', 'dts_idx', default=0, show_default=True, type=int, help='0-based index of the Date/Time')
@click.option('-y', 'val_idx', default=1, show_default=True, type=int, help='0-based index of the Measurement Value')
def histogram(filename, dts_idx, val_idx):
    """
    Generates a histogram plot using the data from FILENAME.csv.

    The plotter uses the Date/Time column for the X-axis and the
    measurement value for the Y-axis. It assumes column=0 to be
    the Date/Time column and column=1 to be the measurement value
    column. Pass in --dts and --val to specify different indices.

    The plotter currently does not support CSV with headers.
    """
    plotter = Histogram(filename)
    plotter.plot(index_col=dts_idx, value_col=val_idx)


# ------------------------------------------------------------------------------
# CLI commands for testing
# ------------------------------------------------------------------------------


@click.group()
def test_cmds():
    pass


@test_cmds.command(short_help='Generates sample files for testing')
@click.argument('filename')
@click.option('--nrows', show_default=True, default=100, help='Number of rows')
@click.option('--ncols', show_default=True, default=3, help='Number of cols')
def examples(filename, nrows, ncols):
    """
    Generates an out/FILENAME.csv with random values.

    The CSV file will have 100 rows and 3 columns.
    The 1st column contains datetime values.
    The 2nd to nth column contains random float values
    forming a gaussian distribution in the range 1-10.
    """
    gaussian.generate(filename, nrows, ncols)


# ------------------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------------------

cli = click.CommandCollection(
    sources=[
        plot_cmds,
        test_cmds,
    ],
    help='Shows interactive plots to visualize data from CSV files.',
)
